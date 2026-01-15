"""
Core logic for yt-dlp GUI.
Handles JS runtime detection and downloader option construction.
"""

from __future__ import annotations

import os
import shlex
from datetime import datetime
from typing import Any, Dict, List, Optional

from yt_dlp.utils._jsruntime import BunJsRuntime, DenoJsRuntime, NodeJsRuntime, QuickJsRuntime

from .logger import MyLogger


class ExecutablePicker:
    """
    Utility class to find and verify external executables using yt-dlp internal logic.
    """

    @staticmethod
    def detect_js_runtime() -> Optional[str]:
        """Detect JS runtime."""
        return detect_js_runtime()

    @staticmethod
    def detect_ffmpeg(path: Optional[str] = None) -> Dict[str, Any]:
        """Detect FFmpeg/FFprobe."""
        return get_ffmpeg_info(path)


def detect_js_runtime() -> Optional[str]:
    """
    Detect the available JavaScript runtime using yt-dlp internal logic.

    @return: Name of the detected runtime or None
    """
    # Priority order: Deno, Bun, Node, QuickJS
    runtimes = [
        DenoJsRuntime(),
        BunJsRuntime(),
        NodeJsRuntime(),
        QuickJsRuntime(),
    ]
    for rt in runtimes:
        try:
            if rt.info and rt.info.supported:
                return rt.info.name
        except Exception:
            continue
    return None


def get_ffmpeg_info(ffmpeg_location: Optional[str] = None) -> Dict[str, Any]:
    """
    Detect FFmpeg info using yt-dlp's FFmpegPostProcessor.

    @param ffmpeg_location: Optional path to ffmpeg folder or executable
    @return: Dictionary with availability, path, and version
    """
    from yt_dlp.postprocessor.ffmpeg import FFmpegPostProcessor
    
    # We need a dummy downloader or None
    pp = FFmpegPostProcessor()
    if ffmpeg_location:
        # Manually inject location if provided
        pp._ffmpeg_location.set(ffmpeg_location)
        pp._paths = pp._determine_executables()
        
    return {
        'available': pp.available,
        'path': pp.executable,
        'version': pp._version if pp.available else None,
        'ffprobe_available': pp.probe_available,
        'ffprobe_path': pp.probe_executable,
        'ffprobe_version': pp._probe_version if pp.probe_available else None,
    }


def build_ydl_opts(ui_data: Dict[str, Any], gui: Any) -> Dict[str, Any]:
    """
    Build the yt-dlp options dictionary from GUI input data.

    @param ui_data: Dictionary containing all UI field values
    @param gui: Reference to the GUI instance for logger and hooks
    @return: yt-dlp options dictionary
    """
    path = ui_data.get('output_dir', os.getcwd())
    
    # Configure output template
    custom_tmpl = ui_data.get('custom_template', '').strip()
    if ui_data.get('custom_template_active') and custom_tmpl:
        out_tmpl = os.path.join(path, custom_tmpl)
    elif ui_data.get('year_folder'):
        out_tmpl = os.path.join(path, '%(upload_date>%Y)s', '%(title)s.%(ext)s')
    else:
        out_tmpl = os.path.join(path, '%(title)s.%(ext)s')

    # Basic Options
    ydl_opts: Dict[str, Any] = {
        'outtmpl': out_tmpl,
        'logger': MyLogger(gui),
        'progress_hooks': [gui.progress_hook],
        'writethumbnail': ui_data.get('embed_thumbnail') or ui_data.get('write_thumbnail_disk'),
        'addmetadata': ui_data.get('embed_metadata'),
        'writesubtitles': ui_data.get('embed_subs'),
        'addchapters': ui_data.get('embed_chapters'),
        'writedescription': ui_data.get('write_desc'),
        'writeinfojson': ui_data.get('write_info'),
        'nopart': not ui_data.get('part_files'),
        'restrictfilenames': ui_data.get('restrict_filenames'),
        'overwrites': ui_data.get('force_overwrite'),
    }

    # Post Processors
    postprocessors: List[Dict[str, Any]] = []
    if ui_data.get('embed_thumbnail'):
        postprocessors.append({'key': 'EmbedThumbnail'})

    sponsorblock_cats = ui_data.get('sponsorblock', '').strip()
    if sponsorblock_cats:
        postprocessors.append({
            'key': 'SponsorBlock',
            'categories': [c.strip() for c in sponsorblock_cats.split(',')],
            'when': 'after_filter',
        })

    # Format Selection
    mode = ui_data.get('format_mode')
    if mode == 'Audio Only':
        fmt = ui_data.get('audio_ext')
        ydl_opts['format'] = 'bestaudio/best'
        postprocessors.append({
            'key': 'FFmpegExtractAudio',
            'preferredcodec': fmt if fmt != 'best' else 'mp3',
        })
    else:
        # Video + Audio
        vid_ext = ui_data.get('video_ext', 'mp4')
        quality = ui_data.get('quality', 'Best')

        q_map = {
            'Best': '',
            '2160p (4K)': '[height<=2160]',
            '1440p (2K)': '[height<=1440]',
            '1080p': '[height<=1080]',
            '720p': '[height<=720]',
            '480p': '[height<=480]',
        }
        height_constraint = q_map.get(quality, '')

        ydl_opts['merge_output_format'] = vid_ext

        if height_constraint:
            h_val = height_constraint.replace('[height<=', '').replace(']', '')
            ydl_opts['format_sort'] = [f'res:{h_val}', f'ext:{vid_ext}']
        else:
            ydl_opts['format_sort'] = [f'ext:{vid_ext}']

    if postprocessors:
        ydl_opts['postprocessors'] = postprocessors

    # Network
    if ui_data.get('rate_limit'):
        ydl_opts['ratelimit'] = ui_data['rate_limit']
    
    if ui_data.get('timeout'):
        try:
            ydl_opts['socket_timeout'] = float(ui_data['timeout'])
        except (ValueError, TypeError):
            pass

    if ui_data.get('source_ip'):
        ydl_opts['source_address'] = ui_data['source_ip']

    # Proxy
    proxy = ui_data.get('proxy_override', '').strip() or ui_data.get('proxy_config', '').strip()
    if proxy:
        ydl_opts['proxy'] = proxy

    browser = ui_data.get('browser', 'none')
    if browser != 'none':
        ydl_opts['cookiesfrombrowser'] = (browser,)

    if ui_data.get('user_agent'):
        ydl_opts['user_agent'] = ui_data['user_agent']

    cookies_file = ui_data.get('cookies_path', '').strip()
    if cookies_file and os.path.exists(cookies_file) and browser == 'none':
        ydl_opts['cookiefile'] = cookies_file

    # FFmpeg Location
    ffmpeg_loc = ui_data.get('ffmpeg_path', '').strip()
    if ffmpeg_loc:
        ydl_opts['ffmpeg_location'] = ffmpeg_loc

    # Filters
    for key in ['playlist_items', 'date', 'datebefore', 'dateafter', 'min_filesize', 'max_filesize', 'match_filter']:
        if ui_data.get(key):
            ydl_opts[key] = ui_data[key]

    # Advanced / Retries
    if ui_data.get('retries'):
        try:
            ydl_opts['retries'] = int(ui_data['retries'])
        except (ValueError, TypeError):
            pass

    if ui_data.get('wait_video'):
        try:
            sec = int(ui_data['wait_video'])
            ydl_opts['wait_for_video'] = (sec, sec)
        except (ValueError, TypeError):
            pass

    if ui_data.get('live_start'):
        ydl_opts['live_from_start'] = True

    if ui_data.get('embed_subs') and ui_data.get('sub_langs'):
        ydl_opts['subtitleslangs'] = ui_data['sub_langs'].split(',')

    if ui_data.get('legacy_ssl'):
        ydl_opts['legacy_server_connect'] = True

    # Extractor Args (Music Optimization)
    extractor_args: Dict[str, Any] = {}
    if ui_data.get('music_mode'):
        current_timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        extractor_args = {
            'youtubetab': {'skip': ['webpage']},
            'youtube': {
                'player_skip': ['webpage', 'configs'],
                'visitor_data': [current_timestamp],
            },
        }

    data_sync_id = ui_data.get('data_sync_id', '').strip()
    if data_sync_id:
        if 'youtube' not in extractor_args:
            extractor_args['youtube'] = {}
        extractor_args['youtube']['data_sync_id'] = [data_sync_id]

    if extractor_args:
        ydl_opts['extractor_args'] = extractor_args

    # Custom Extra Arguments
    extra_args = ui_data.get('extra_args', '').strip()
    if extra_args:
        from yt_dlp.options import parseOpts
        try:
            # shlex.split helps handle quoted arguments correctly
            args_list = shlex.split(extra_args)
            _, _, _, extra_ydl_opts = parseOpts(args_list)
            # Merge extra_ydl_opts into ydl_opts
            ydl_opts.update(extra_ydl_opts)
        except Exception as e:
            # In a real app, we might want to log this or notify the user
            print(f"Error parsing extra arguments: {e}")

    return ydl_opts


def get_command_preview(ui_data: Dict[str, Any]) -> str:
    """
    Generate a CLI command preview string based on the current UI data.
    """
    cmd = ['yt-dlp']
    
    # URL
    url = ui_data.get('video_url', '').strip()
    if not url:
        url = 'URL'
    
    # Basic options that map simply to CLI
    if ui_data.get('format_mode') == 'Audio Only':
        cmd.extend(['-f', 'ba/b', '-x', '--audio-format', ui_data.get('audio_ext', 'mp3')])
    else:
        ext = ui_data.get('video_ext', 'mp4')
        quality = ui_data.get('quality', 'Best')
        q_map = {
            '2160p (4K)': '[height<=2160]',
            '1440p (2K)': '[height<=1440]',
            '1080p': '[height<=1080]',
            '720p': '[height<=720]',
            '480p': '[height<=480]',
        }
        h = q_map.get(quality, '')
        cmd.extend(['--merge-output-format', ext])
        if h:
            cmd.extend(['-S', f'res:{h.replace("[height<=", "").replace("]", "")},ext:{ext}'])
        else:
            cmd.extend(['-S', f'ext:{ext}'])

    # Directory and Template
    out_dir = ui_data.get('output_dir', '.')
    custom_tmpl = ui_data.get('custom_template', '').strip()
    if ui_data.get('custom_template_active') and custom_tmpl:
        cmd.extend(['-o', os.path.join(out_dir, custom_tmpl)])
    elif ui_data.get('year_folder'):
        cmd.extend(['-o', os.path.join(out_dir, '%(upload_date>%Y)s', '%(title)s.%(ext)s')])
    else:
        cmd.extend(['-o', os.path.join(out_dir, '%(title)s.%(ext)s')])

    # Flags
    if ui_data.get('embed_thumbnail'): cmd.append('--embed-thumbnail')
    if ui_data.get('embed_metadata'): cmd.append('--embed-metadata')
    if ui_data.get('embed_subs'): cmd.append('--embed-subs')
    if ui_data.get('embed_chapters'): cmd.append('--embed-chapters')
    if not ui_data.get('part_files'): cmd.append('--no-part')
    if ui_data.get('restrict_filenames'): cmd.append('--restrict-filenames')
    if ui_data.get('force_overwrite'): cmd.append('--force-overwrites')

    # Subtitle languages
    if ui_data.get('embed_subs') and ui_data.get('sub_langs'):
        cmd.extend(['--sub-langs', ui_data['sub_langs']])

    # SponsorBlock
    sb = ui_data.get('sponsorblock', '').strip()
    if sb:
        cmd.extend(['--sponsorblock-mark', sb])

    # Extra arguments
    extra = ui_data.get('extra_args', '').strip()
    if extra:
        cmd.append(extra)

    cmd.append(f'"{url}"')
    
    return ' '.join(cmd)
