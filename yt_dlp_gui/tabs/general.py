"""
General settings tab for yt-dlp GUI.
"""

import tkinter as tk
from tkinter import ttk
from typing import Any, Dict

from ..i18n import _


class GeneralTab(ttk.Frame):
    """
    Tab for general download settings.
    """

    def __init__(self, master: ttk.Notebook, **kwargs: Any) -> None:
        """
        Initialize the General tab.
        """
        super().__init__(master, **kwargs)
        self.pack(fill=tk.BOTH, expand=True)

        frame = ttk.Frame(self, padding=20)
        frame.pack(fill=tk.BOTH, expand=True)
        frame.columnconfigure(1, weight=1)

        # Row 0: Format Mode
        self.format_label = ttk.Label(frame, text=_('Format:'))
        self.format_label.grid(row=0, column=0, sticky=tk.W, pady=5)
        self.format_mode_var = tk.StringVar(value='Video+Audio')
        self.mode_cb = ttk.Combobox(
            frame, textvariable=self.format_mode_var, values=['Video+Audio', 'Audio Only'], state='readonly',
        )
        self.mode_cb.grid(row=0, column=1, sticky=tk.EW, padx=10, pady=5)
        self.mode_cb.bind('<<ComboboxSelected>>', self.on_mode_change)

        # Row 1: Video Format
        self.vid_fmt_label = ttk.Label(frame, text=_('Video Extension:'))
        self.vid_fmt_label.grid(row=1, column=0, sticky=tk.W, pady=5)
        self.video_ext_var = tk.StringVar(value='mp4')
        self.video_ext_cb = ttk.Combobox(
            frame, textvariable=self.video_ext_var, values=['mp4', 'mkv', 'webm'], state='readonly',
        )
        self.video_ext_cb.grid(row=1, column=1, sticky=tk.EW, padx=10, pady=5)

        # Row 2: Audio Format
        self.aud_fmt_label = ttk.Label(frame, text=_('Audio Extension:'))
        self.aud_fmt_label.grid(row=2, column=0, sticky=tk.W, pady=5)
        self.audio_ext_var = tk.StringVar(value='mp3')
        self.audio_ext_cb = ttk.Combobox(
            frame, textvariable=self.audio_ext_var, values=['mp3', 'm4a', 'wav', 'flac', 'best'], state='readonly',
        )
        self.audio_ext_cb.grid(row=2, column=1, sticky=tk.EW, padx=10, pady=5)

        # Row 3: Quality
        self.qual_label = ttk.Label(frame, text=_('Quality:'))
        self.qual_label.grid(row=3, column=0, sticky=tk.W, pady=5)
        self.quality_var = tk.StringVar(value='Best')
        self.quality_cb = ttk.Combobox(
            frame, textvariable=self.quality_var,
            values=['Best', '2160p (4K)', '1440p (2K)', '1080p', '720p', '480p'], state='readonly',
        )
        self.quality_cb.grid(row=3, column=1, sticky=tk.EW, padx=10, pady=5)

        # Separator
        ttk.Separator(frame, orient=tk.HORIZONTAL).grid(row=4, column=0, columnspan=2, sticky=tk.EW, pady=15)

        # Checkboxes
        self.music_opt_var = tk.BooleanVar()
        self.music_opt_check = ttk.Checkbutton(frame, text=_('Music Mode (Optimized)'), variable=self.music_opt_var)
        self.music_opt_check.grid(row=5, column=0, columnspan=2, sticky=tk.W, pady=5)

        self.year_folder_var = tk.BooleanVar(value=True)
        self.year_folder_check = ttk.Checkbutton(frame, text=_('Organize by Year'), variable=self.year_folder_var)
        self.year_folder_check.grid(row=6, column=0, columnspan=2, sticky=tk.W, pady=5)

        # Custom Template
        self.custom_tmpl_var = tk.BooleanVar()
        self.custom_tmpl_check = ttk.Checkbutton(frame, text=_('Custom Output Template:'), variable=self.custom_tmpl_var)
        self.custom_tmpl_check.grid(row=7, column=0, sticky=tk.W, pady=5)
        self.custom_tmpl_check.bind('<Button-1>', lambda e: self.root.after(10, self.on_tmpl_toggle))

        self.custom_tmpl_str_var = tk.StringVar(value='%(title)s.%(ext)s')
        self.custom_tmpl_entry = tk.Entry(
            frame, textvariable=self.custom_tmpl_str_var, bg='#3e3e3e', fg='white', 
            insertbackground='white', relief=tk.FLAT, state=tk.DISABLED
        )
        self.custom_tmpl_entry.grid(row=7, column=1, sticky=tk.EW, padx=10, pady=5, ipady=3)

        self.on_mode_change(None)

    def on_mode_change(self, _: Any) -> None:
        """Handle format mode change (Video+Audio vs Audio Only)."""
        mode = self.format_mode_var.get()
        if mode == 'Audio Only':
            self.video_ext_cb.configure(state=tk.DISABLED)
            self.quality_cb.configure(state=tk.DISABLED)
            self.audio_ext_cb.configure(state='readonly')
        else:
            self.video_ext_cb.configure(state='readonly')
            self.quality_cb.configure(state='readonly')
            self.audio_ext_cb.configure(state=tk.DISABLED)

    def on_tmpl_toggle(self, *args: Any) -> None:
        """Handle custom template checkbox toggle."""
        # Use after to wait for var to update
        self.after(20, self._update_tmpl_state)

    def _update_tmpl_state(self) -> None:
        if self.custom_tmpl_var.get():
            self.custom_tmpl_entry.configure(state=tk.NORMAL)
            self.year_folder_check.configure(state=tk.DISABLED)
        else:
            self.custom_tmpl_entry.configure(state=tk.DISABLED)
            self.year_folder_check.configure(state=tk.NORMAL)

    def update_texts(self) -> None:
        """Update localized texts."""
        self.format_label.config(text=_('Format:'))
        self.vid_fmt_label.config(text=_('Video Extension:'))
        self.aud_fmt_label.config(text=_('Audio Extension:'))
        self.qual_label.config(text=_('Quality:'))
        self.music_opt_check.config(text=_('Music Mode (Optimized)'))
        self.year_folder_check.config(text=_('Organize by Year'))
        self.custom_tmpl_check.config(text=_('Custom Output Template:'))

    def get_data(self) -> Dict[str, Any]:
        """Collect tab data."""
        return {
            'format_mode': self.format_mode_var.get(),
            'video_ext': self.video_ext_var.get(),
            'audio_ext': self.audio_ext_var.get(),
            'quality': self.quality_var.get(),
            'music_mode': self.music_opt_var.get(),
            'year_folder': self.year_folder_var.get(),
            'custom_template_active': self.custom_tmpl_var.get(),
            'custom_template': self.custom_tmpl_str_var.get(),
        }
