"""
Tests for yt-dlp GUI logic.
"""

import unittest
from typing import Any, Dict

from yt_dlp_gui.logic import ExecutablePicker, build_ydl_opts


class DummyGUI:
    def progress_hook(self, d: Any) -> None:
        pass


class TestGUILogic(unittest.TestCase):
    def test_build_ydl_opts_basic(self) -> None:
        gui = DummyGUI()
        ui_data = {
            'format_mode': 'Video+Audio',
            'video_ext': 'mp4',
            'quality': '1080p',
            'part_files': True,
        }
        opts = build_ydl_opts(ui_data, gui)
        self.assertEqual(opts['merge_output_format'], 'mp4')
        self.assertIn('res:1080', str(opts['format_sort']))

    def test_build_ydl_opts_audio(self) -> None:
        gui = DummyGUI()
        ui_data = {
            'format_mode': 'Audio Only',
            'audio_ext': 'mp3',
        }
        opts = build_ydl_opts(ui_data, gui)
        self.assertEqual(opts['format'], 'bestaudio/best')
        # Check postprocessors
        found_audio_pp = False
        for pp in opts.get('postprocessors', []):
            if pp['key'] == 'FFmpegExtractAudio' and pp['preferredcodec'] == 'mp3':
                found_audio_pp = True
        self.assertTrue(found_audio_pp)

    def test_executable_picker(self) -> None:
        # Just check it doesn't crash
        js = ExecutablePicker.detect_js_runtime()
        self.assertIsInstance(js, (str, type(None)))


if __name__ == '__main__':
    unittest.main()
