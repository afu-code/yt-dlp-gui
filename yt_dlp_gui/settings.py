"""
Settings dialog for yt-dlp GUI.
Allows users to configure global settings like output directory and language.
"""

import os
import tkinter as tk
from tkinter import filedialog, ttk
from typing import Any, Callable, Dict

from .i18n import LANGUAGES, _
from .widgets import ModernButton, SecondaryButton


class SettingsWindow(tk.Toplevel):
    """
    Settings dialog window with tabbed interface.
    """

    def __init__(
        self,
        parent: tk.Widget,
        current_config: Dict[str, Any],
        callback: Callable[[Dict[str, Any]], None],
    ) -> None:
        """
        Initialize the settings window.

        @param parent: Parent window
        @param current_config: Current configuration dictionary
        @param callback: Function to call when settings are saved
        """
        super().__init__(parent)
        self.title(_('Settings'))

        # Center the window
        window_width = 700
        window_height = 600
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        center_x = int((screen_width - window_width) / 2)
        center_y = int((screen_height - window_height) / 2)
        self.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
        self.configure(bg='#2d2d2d')

        self.callback = callback
        self.result = current_config.copy()

        self.transient(parent)
        self.grab_set()

        # Notebook for categorized settings
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=(10, 0))

        # --- Tab 1: General ---
        self.tab_general = ttk.Frame(self.notebook, padding=20)
        self.notebook.add(self.tab_general, text=_('General'))

        # Language
        ttk.Label(self.tab_general, text=_('Language:')).pack(anchor=tk.W, pady=(0, 5))
        self.lang_var = tk.StringVar(value=self.result.get('language', 'en'))
        lang_combo = ttk.Combobox(self.tab_general, state='readonly')
        lang_combo['values'] = list(LANGUAGES.values())
        rev_lang_map = {v: k for k, v in LANGUAGES.items()}
        lang_combo.set(LANGUAGES.get(self.lang_var.get(), 'English'))
        lang_combo.bind('<<ComboboxSelected>>', lambda _: self.lang_var.set(rev_lang_map.get(lang_combo.get(), 'en')))
        lang_combo.pack(fill=tk.X, pady=(0, 15))

        # Theme
        ttk.Label(self.tab_general, text=_('Theme:')).pack(anchor=tk.W, pady=(0, 5))
        self.theme_var = tk.StringVar(value=self.result.get('theme', 'dark'))
        theme_map = {'dark': _('Dark'), 'light': _('Light')}
        rev_theme_map = {v: k for k, v in theme_map.items()}
        theme_combo = ttk.Combobox(self.tab_general, state='readonly', values=list(theme_map.values()))
        theme_combo.set(theme_map.get(self.theme_var.get(), _('Dark')))
        theme_combo.bind('<<ComboboxSelected>>', lambda _: self.theme_var.set(rev_theme_map.get(theme_combo.get(), 'dark')))
        theme_combo.pack(fill=tk.X, pady=(0, 15))

        # Output Directory
        ttk.Label(self.tab_general, text=_('Output Directory:')).pack(anchor=tk.W, pady=(0, 5))
        path_frame = ttk.Frame(self.tab_general)
        path_frame.pack(fill=tk.X, pady=(0, 15))
        self.path_var = tk.StringVar(value=self.result.get('output_dir', os.getcwd()))
        tk.Entry(
            path_frame, textvariable=self.path_var, bg='#3e3e3e', fg='white',
            insertbackground='white', relief=tk.FLAT, font=('Segoe UI', 10),
        ).pack(side=tk.LEFT, fill=tk.X, expand=True, ipady=5)
        SecondaryButton(path_frame, text=_('Browse'), command=self.browse_path).pack(side=tk.RIGHT, padx=(10, 0))

        # Cookies
        ttk.Label(self.tab_general, text=_('Cookies File:')).pack(anchor=tk.W, pady=(0, 5))
        cookies_frame = ttk.Frame(self.tab_general)
        cookies_frame.pack(fill=tk.X, pady=(0, 15))
        self.cookies_var = tk.StringVar(value=self.result.get('cookies_path', ''))
        tk.Entry(
            cookies_frame, textvariable=self.cookies_var, bg='#3e3e3e', fg='white',
            insertbackground='white', relief=tk.FLAT, font=('Segoe UI', 10),
        ).pack(side=tk.LEFT, fill=tk.X, expand=True, ipady=5)
        SecondaryButton(cookies_frame, text=_('Browse'), command=self.browse_cookies).pack(side=tk.RIGHT, padx=(10, 0))

        # Proxy
        ttk.Label(self.tab_general, text=_('Proxy URL:')).pack(anchor=tk.W, pady=(0, 5))
        self.proxy_var = tk.StringVar(value=self.result.get('proxy_url', ''))
        tk.Entry(
            self.tab_general, textvariable=self.proxy_var, bg='#3e3e3e', fg='white',
            insertbackground='white', relief=tk.FLAT, font=('Segoe UI', 10),
        ).pack(fill=tk.X, pady=(0, 15), ipady=5)

        # --- Tab 2: Tools ---
        self.tab_tools = ttk.Frame(self.notebook, padding=20)
        self.notebook.add(self.tab_tools, text=_('Tools'))

        # FFmpeg Location
        ttk.Label(self.tab_tools, text=_('FFmpeg Location:')).pack(anchor=tk.W, pady=(0, 5))
        ffmpeg_frame = ttk.Frame(self.tab_tools)
        ffmpeg_frame.pack(fill=tk.X, pady=(0, 15))
        self.ffmpeg_var = tk.StringVar(value=self.result.get('ffmpeg_path', ''))
        tk.Entry(
            ffmpeg_frame, textvariable=self.ffmpeg_var, bg='#3e3e3e', fg='white',
            insertbackground='white', relief=tk.FLAT, font=('Segoe UI', 10),
        ).pack(side=tk.LEFT, fill=tk.X, expand=True, ipady=5)
        SecondaryButton(ffmpeg_frame, text=_('Browse'), command=self.browse_ffmpeg).pack(side=tk.RIGHT, padx=(10, 0))

        # Detection Info
        self.tools_info_frame = ttk.LabelFrame(self.tab_tools, text='Detection', padding=10)
        self.tools_info_frame.pack(fill=tk.X, pady=10)
        
        self.ffmpeg_status_label = ttk.Label(self.tools_info_frame, text='')
        self.ffmpeg_status_label.pack(anchor=tk.W)
        self.ffprobe_status_label = ttk.Label(self.tools_info_frame, text='')
        self.ffprobe_status_label.pack(anchor=tk.W)

        # Data Sync ID (Moved to Tools or keep in General? Let's put in Tools/Core)
        ttk.Label(self.tab_tools, text=_('Data Sync ID:')).pack(anchor=tk.W, pady=(10, 5))
        self.sync_var = tk.StringVar(value=self.result.get('data_sync_id', ''))
        tk.Entry(
            self.tab_tools, textvariable=self.sync_var, bg='#3e3e3e', fg='white',
            insertbackground='white', relief=tk.FLAT, font=('Segoe UI', 10),
        ).pack(fill=tk.X, pady=(0, 15), ipady=5)

        # Bottom Buttons
        btn_frame = ttk.Frame(self)
        btn_frame.pack(fill=tk.X, padx=20, pady=20)
        ModernButton(btn_frame, text=_('Save Settings'), command=self.save, width=15, pady=8, font=('Segoe UI', 10, 'bold')).pack(side=tk.RIGHT, padx=5)
        SecondaryButton(btn_frame, text=_('Cancel'), command=self.destroy, width=10, pady=8, font=('Segoe UI', 10, 'bold'), padx=20).pack(side=tk.RIGHT, padx=5)

        # Initial detection
        self.update_tool_info()
        self.ffmpeg_var.trace_add('write', lambda *_: self.update_tool_info())

    def update_tool_info(self) -> None:
        """Update detection labels for ffmpeg/ffprobe."""
        from .logic import ExecutablePicker
        info = ExecutablePicker.detect_ffmpeg(self.ffmpeg_var.get())
        
        f_ver = info['version'] or _('Not Found')
        p_ver = info['ffprobe_version'] or _('Not Found')
        
        self.ffmpeg_status_label.config(text=_('FFmpeg Status: {}').format(f_ver))
        self.ffprobe_status_label.config(text=_('FFprobe Status: {}').format(p_ver))

    def browse_path(self) -> None:
        """Open directory browser for output directory."""
        p = filedialog.askdirectory()
        if p:
            self.path_var.set(p)

    def browse_cookies(self) -> None:
        """Open file browser for cookies file."""
        f = filedialog.askopenfilename()
        if f:
            self.cookies_var.set(f)

    def browse_ffmpeg(self) -> None:
        """Open directory browser for FFmpeg folder."""
        p = filedialog.askdirectory()
        if p:
            self.ffmpeg_var.set(p)

    def save(self) -> None:
        """Save settings and close the window."""
        self.result.update({
            'language': self.lang_var.get(),
            'theme': self.theme_var.get(),
            'output_dir': self.path_var.get(),
            'cookies_path': self.cookies_var.get(),
            'data_sync_id': self.sync_var.get(),
            'proxy_url': self.proxy_var.get(),
            'ffmpeg_path': self.ffmpeg_var.get(),
        })
        self.callback(self.result)
        self.destroy()

