"""
Main GUI application for yt-dlp.
Handles UI layout, user input, and orchestrates the download process.
"""

from __future__ import annotations

import os
import threading
import tkinter as tk
from tkinter import messagebox, ttk
from typing import Any, Dict, Optional

import yt_dlp
from yt_dlp.utils import DownloadError

from .config import load_config, save_config
from .logic import ExecutablePicker, build_ydl_opts, get_command_preview
from .settings import SettingsWindow
from .tabs import AdvancedTab, FiltersTab, GeneralTab, NetworkTab, PostTab
from .i18n import set_language, _
from .widgets import ModernButton, PlaceholderEntry, SecondaryButton, Tooltip


class YTDownloaderGUI:
    """
    Main application class for the yt-dlp Graphical User Interface.
    """

    def __init__(self, root: tk.Tk) -> None:
        """
        Initialize the GUI.

        @param root: The root Tkinter window
        """
        self.root = root

        # Load Config and set language
        self.config: Dict[str, Any] = load_config()
        set_language(self.config.get('language', 'en'))

        self.root.title(_('yt-dlp Visual Downloader'))
        # Center the window
        window_width = 1000
        window_height = 800
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        center_x = int((screen_width - window_width) / 2)
        center_y = int((screen_height - window_height) / 2)
        self.root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
        self.root.configure(bg='#2d2d2d')

        # Styles
        self._setup_styles()

        # UI Components
        self._create_header()
        self._create_url_section()
        self._create_tabs()
        self._create_bottom_section()
        self._create_log_area()

        # Initialize JS Runtime info
        self.js_runtime: Optional[str] = ExecutablePicker.detect_js_runtime()
        self._update_js_label()

    def _setup_styles(self) -> None:
        """Initialize ttk styles."""
        self.style = ttk.Style()
        self.style.theme_use('clam')

        self.style.configure('TLabel', background='#2d2d2d', foreground='#ffffff', font=('Segoe UI', 10))
        self.style.configure('TEntry', fieldbackground='#3e3e3e', foreground='#ffffff', borderwidth=0)
        self.style.configure('TFrame', background='#2d2d2d')
        self.style.configure('TCheckbutton', background='#2d2d2d', foreground='#ffffff', font=('Segoe UI', 10))
        self.style.map('TCheckbutton', background=[('active', '#2d2d2d')])
        self.style.configure('TNotebook', background='#2d2d2d', borderwidth=0)
        self.style.configure(
            'TNotebook.Tab', background='#3e3e3e', foreground='#ffffff', padding=[15, 8], font=('Segoe UI', 10),
        )
        self.style.map('TNotebook.Tab', background=[('selected', '#505050')], foreground=[('selected', '#ffffff')])

        # Progress Bar Style
        self.style.configure(
            'Horizontal.TProgressbar', background='#007acc', troughcolor='#3e3e3e', bordercolor='#2d2d2d',
            lightcolor='#007acc', darkcolor='#007acc',
        )

    def _create_header(self) -> None:
        """Create the header frame with title and settings button."""
        header_frame = tk.Frame(self.root, bg='#2d2d2d')
        header_frame.pack(fill=tk.X, pady=15, padx=25)

        header_font = ('Segoe UI', 18, 'bold')
        self.header_label = tk.Label(header_frame, text=_('YouTube Downloader'), bg='#2d2d2d', fg='#ffffff', font=header_font)
        self.header_label.pack(side=tk.LEFT)

        self.settings_btn = SecondaryButton(header_frame, text=_('⚙ Settings'), command=self.open_settings)
        self.settings_btn.pack(side=tk.RIGHT)

    def _create_url_section(self) -> None:
        """Create the URL input section."""
        url_frame = tk.Frame(self.root, bg='#2d2d2d')
        url_frame.pack(fill=tk.X, padx=25, pady=(0, 10))

        self.url_label_widget = ttk.Label(url_frame, text=_('Video URL:'))
        self.url_label_widget.pack(anchor=tk.W, pady=(0, 5))

        url_input_frame = tk.Frame(url_frame, bg='#2d2d2d')
        url_input_frame.pack(fill=tk.X)

        self.url_var = tk.StringVar()
        self.url_entry = PlaceholderEntry(
            url_input_frame, textvariable=self.url_var, bg='#3e3e3e', fg='white', 
            insertbackground='white', relief=tk.FLAT, font=('Segoe UI', 11),
            placeholder=_('https://www.youtube.com/watch?v=...'),
        )
        self.url_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, ipady=6)

        self.download_btn = ModernButton(
            url_input_frame, text=_('START DOWNLOAD'), command=self.start_download_thread, 
            pady=5, font=('Segoe UI', 11, 'bold'),
        )
        Tooltip(self.download_btn, _('Click to begin downloading the video or playlist'))
        self.download_btn.pack(side=tk.RIGHT, padx=(10, 0))

    def _create_tabs(self) -> None:
        """Create the notebook and tabs."""
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=25, pady=(0, 10))

        self.tab_general = GeneralTab(self.notebook)
        self.tab_network = NetworkTab(self.notebook)
        self.tab_filters = FiltersTab(self.notebook)
        self.tab_post = PostTab(self.notebook)
        self.tab_advanced = AdvancedTab(self.notebook)

        self.notebook.add(self.tab_general, text=_('General'))
        self.notebook.add(self.tab_network, text=_('Network'))
        self.notebook.add(self.tab_filters, text=_('Filters'))
        self.notebook.add(self.tab_post, text=_('Post-Processing'))
        self.notebook.add(self.tab_advanced, text=_('Advanced'))

    def _create_bottom_section(self) -> None:
        """Create status, JS indicator, and progress bar."""
        self.bottom_frame = ttk.Frame(self.root)
        self.bottom_frame.pack(fill=tk.X, padx=25, pady=10)

        self.status_label = ttk.Label(self.bottom_frame, text=_('Ready'))
        self.status_label.pack(anchor=tk.W, pady=(0, 5))

        self.js_label = tk.Label(self.bottom_frame, text='', bg='#2d2d2d', font=('Segoe UI', 9))
        self.js_label.pack(anchor=tk.W)

        self.progress_bar = ttk.Progressbar(self.bottom_frame, orient=tk.HORIZONTAL, length=100, mode='determinate')
        self.progress_bar.pack(fill=tk.X, pady=5)

        # Command Preview
        self.preview_frame = tk.Frame(self.root, bg='#2d2d2d')
        self.preview_frame.pack(fill=tk.X, padx=25, pady=(5, 0))
        
        self.preview_label = ttk.Label(self.preview_frame, text=_('Command Preview:'))
        self.preview_label.pack(anchor=tk.W)
        
        self.preview_text = tk.Text(
            self.preview_frame, height=2, bg='#1e1e1e', fg='#9cdcfe', relief=tk.FLAT, 
            font=('Consolas', 9), state=tk.DISABLED, padx=5, pady=5
        )
        self.preview_text.pack(fill=tk.X)
        
        # Initial preview
        self.root.after(100, self.update_private_preview)

    def _create_log_area(self) -> None:
        """Create the text area for logs."""
        log_frame = ttk.Frame(self.root)
        log_frame.pack(fill=tk.BOTH, expand=True, padx=25, pady=(0, 15))
        self.log_label_widget = ttk.Label(log_frame, text=_('Log Output:'))
        self.log_label_widget.pack(anchor=tk.W)
        self.log_text = tk.Text(
            log_frame, height=6, bg='#1e1e1e', fg='#d4d4d4', relief=tk.FLAT, font=('Consolas', 9), state=tk.DISABLED,
        )
        self.log_text.pack(fill=tk.BOTH, expand=True)

    def _update_js_label(self) -> None:
        """Update the JS runtime label color and text."""
        color = '#4caf50' if self.js_runtime else '#f44336'
        text = _('JS Engine: {}').format(self.js_runtime or _('Missing (Node.js/Deno not found)'))
        self.js_label.config(text=text, fg=color)

    def open_settings(self) -> None:
        """Open the settings window."""
        SettingsWindow(self.root, self.config, self.update_settings)

    def update_settings(self, new_config: Dict[str, Any]) -> None:
        """Callback for when settings are saved."""
        self.config = new_config
        set_language(self.config.get('language', 'en'))
        save_config(self.config)
        self.update_texts()
        messagebox.showinfo(_('⚙ Settings'), _('Settings saved successfully!'))

    def update_texts(self) -> None:
        """Update all UI elements with the current language."""
        self.root.title(_('yt-dlp Visual Downloader'))
        self.header_label.config(text=_('YouTube Downloader'))
        self.settings_btn.config(text=_('⚙ Settings'))
        self.url_label_widget.config(text=_('Video URL:'))
        self.status_label.config(text=_('Ready'))
        self.download_btn.config(text=_('START DOWNLOAD'))
        self.log_label_widget.config(text=_('Log Output:'))
        self.url_entry.placeholder = _('https://www.youtube.com/watch?v=...')
        self.url_entry._add_placeholder()
        self.preview_label.config(text=_('Command Preview:'))

        self.notebook.tab(self.tab_general, text=_('General'))
        self.notebook.tab(self.tab_network, text=_('Network'))
        self.notebook.tab(self.tab_filters, text=_('Filters'))
        self.notebook.tab(self.tab_post, text=_('Post-Processing'))
        self.notebook.tab(self.tab_advanced, text=_('Advanced'))

        self.tab_general.update_texts()
        self.tab_network.update_texts()
        self.tab_filters.update_texts()
        self.tab_post.update_texts()
        self.tab_advanced.update_texts()

        self._update_js_label()
        self.update_private_preview()

    def log(self, message: str) -> None:
        """Append a message to the log area."""
        self.log_text.config(state=tk.NORMAL)
        self.log_text.insert(tk.END, message + '\n')
        self.log_text.see(tk.END)
        self.log_text.config(state=tk.DISABLED)

    def update_status(self, message: str) -> None:
        """Update the status label text."""
        self.status_label.config(text=message)

    def update_progress(self, percent: float) -> None:
        """Update the progress bar value."""
        self.progress_bar['value'] = percent

    def get_ui_data(self) -> Dict[str, Any]:
        """Collect all UI data for logic processing."""
        path = self.config.get('output_dir', '.')
        ui_data = self.config.copy()
        ui_data.update({
            'video_url': self.url_var.get(),
            'output_dir': path,
            'proxy_config': self.config.get('proxy_url', ''),
        })
        ui_data.update(self.tab_general.get_data())
        ui_data.update(self.tab_network.get_data())
        ui_data.update(self.tab_filters.get_data())
        ui_data.update(self.tab_post.get_data())
        ui_data.update(self.tab_advanced.get_data())
        return ui_data

    def update_private_preview(self) -> None:
        """Internal helper to update the command preview text."""
        ui_data = self.get_ui_data()
        cmd = get_command_preview(ui_data)
        
        self.preview_text.config(state=tk.NORMAL)
        self.preview_text.delete(1.0, tk.END)
        self.preview_text.insert(tk.END, cmd)
        self.preview_text.config(state=tk.DISABLED)
        
        # Schedule next update if anything changed (polling approach for simplicity with Entry widgets)
        self.root.after(500, self.update_private_preview)

    def start_download_thread(self) -> None:
        """Start the download in a background thread."""
        url = self.url_var.get().strip()
        if not url:
            messagebox.showwarning(_('Input Error'), _('Please enter a valid URL'))
            return

        # Simple path validation/creation
        path = self.config.get('output_dir', '.')
        if not os.path.exists(path):
            try:
                os.makedirs(path, exist_ok=True)
            except Exception:
                messagebox.showwarning(_('Path Error'), _('Output directory does not exist and cannot be created:\n{}').format(path))
                return

        # Prepare UI
        self.download_btn.config(state=tk.DISABLED, text=_('DOWNLOADING...'))
        self.progress_bar['value'] = 0
        self.log_text.config(state=tk.NORMAL)
        self.log_text.delete(1.0, tk.END)
        self.log_text.config(state=tk.DISABLED)

        # Build data snapshot for the thread
        ui_data = self.get_ui_data()

        thread = threading.Thread(target=self.download, args=(ui_data,))
        thread.daemon = True
        thread.start()

    def download(self, ui_data: Dict[str, Any]) -> None:
        """The actual download process (runs in thread)."""
        url = ui_data['video_url']
        ydl_opts = build_ydl_opts(ui_data, self)
        
        # Batch support
        if os.path.isfile(url):
            ydl_opts['batchfile'] = url
            urls = [] # yt-dlp will read from batchfile
        else:
            urls = [url]

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download(urls)
            
            self.root.after(0, lambda: self.log(_('Success')))
            self.root.after(0, lambda: self.update_status(_('Completed')))
            self.root.after(0, lambda: messagebox.showinfo(_('Success'), _('Download Finished!')))
        except DownloadError as e:
            self.root.after(0, lambda: self.log(f'{_("Error")}: {e}'))
            self.root.after(0, lambda: self.update_status(_('Error occurred')))
            self.root.after(0, lambda: messagebox.showerror(_('Error'), str(e)))
        except Exception as e:
            self.root.after(0, lambda: self.log(f'Unexpected error: {e}'))
            self.root.after(0, lambda: self.update_status(_('Error occurred')))
            self.root.after(0, lambda: messagebox.showerror(_('Error'), f'An unexpected error occurred: {e}'))
        finally:
            self.root.after(0, lambda: self.download_btn.config(state=tk.NORMAL, text=_('START DOWNLOAD')))

    def progress_hook(self, d: Dict[str, Any]) -> None:
        """Hook called by yt-dlp to report progress."""
        if d['status'] == 'downloading':
            try:
                p_str = d.get('_percent_str', '0%').replace('%', '').strip()
                progress = float(p_str)
                self.root.after(0, lambda: self.update_progress(progress))
                self.root.after(0, lambda: self.update_status(f'Downloading: {d.get("_percent_str")}'))
            except (ValueError, TypeError):
                pass
        elif d['status'] == 'finished':
            self.root.after(0, lambda: self.update_progress(100))
            self.root.after(0, lambda: self.update_status('Download Complete, processing...'))
