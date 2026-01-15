"""
Advanced settings tab for yt-dlp GUI.
"""

import tkinter as tk
from tkinter import ttk
from typing import Any, Dict

from ..i18n import _


class AdvancedTab(ttk.Frame):
    """
    Tab for advanced download options.
    """

    def __init__(self, master: ttk.Notebook, **kwargs: Any) -> None:
        """
        Initialize the Advanced tab.
        """
        super().__init__(master, **kwargs)
        self.pack(fill=tk.BOTH, expand=True)

        frame = ttk.Frame(self, padding=20)
        frame.pack(fill=tk.BOTH, expand=True)
        frame.columnconfigure(1, weight=1)

        # Basic Advanced
        self.legacy_ssl_var = tk.BooleanVar()
        self.legacy_ssl_check = ttk.Checkbutton(frame, text=_('Legacy SSL (Fix EOF)'), variable=self.legacy_ssl_var)
        self.legacy_ssl_check.grid(row=0, column=0, columnspan=2, sticky=tk.W, pady=5)

        self.live_start_var = tk.BooleanVar()
        self.live_start_check = ttk.Checkbutton(frame, text=_('Live From Start'), variable=self.live_start_var)
        self.live_start_check.grid(row=1, column=0, columnspan=2, sticky=tk.W, pady=5)

        self.part_files_var = tk.BooleanVar(value=True)
        self.part_files_check = ttk.Checkbutton(frame, text=_('Use .part files'), variable=self.part_files_var)
        self.part_files_check.grid(row=2, column=0, columnspan=2, sticky=tk.W, pady=5)

        self.restrict_filenames_var = tk.BooleanVar()
        self.restrict_filenames_check = ttk.Checkbutton(
            frame, text=_('Restrict Filenames (ASCII)'), variable=self.restrict_filenames_var,
        )
        self.restrict_filenames_check.grid(row=3, column=0, columnspan=2, sticky=tk.W, pady=5)

        self.force_overwrite_var = tk.BooleanVar()
        self.force_overwrite_check = ttk.Checkbutton(
            frame, text=_('Force Overwrite'), variable=self.force_overwrite_var,
        )
        self.force_overwrite_check.grid(row=4, column=0, columnspan=2, sticky=tk.W, pady=5)

        # Retries
        self.retries_label = ttk.Label(frame, text=_('Retries:'))
        self.retries_label.grid(row=5, column=0, sticky=tk.W, pady=5)
        self.retries_var = tk.StringVar(value='10')
        tk.Entry(
            frame, textvariable=self.retries_var, bg='#3e3e3e', fg='white', insertbackground='white', relief=tk.FLAT,
        ).grid(row=5, column=1, sticky=tk.EW, padx=10, pady=5, ipady=3)

        # Wait for video
        self.wait_video_label = ttk.Label(frame, text=_('Wait for Video (seconds):'))
        self.wait_video_label.grid(row=6, column=0, sticky=tk.W, pady=5)
        self.wait_video_var = tk.StringVar()
        tk.Entry(
            frame, textvariable=self.wait_video_var, bg='#3e3e3e', fg='white', insertbackground='white', relief=tk.FLAT,
        ).grid(row=6, column=1, sticky=tk.EW, padx=10, pady=5, ipady=3)

        # Extra Arguments
        self.extra_args_label = ttk.Label(frame, text=_('Extra Arguments (CLI):'))
        self.extra_args_label.grid(row=7, column=0, sticky=tk.W, pady=5)
        self.extra_args_var = tk.StringVar()
        tk.Entry(
            frame, textvariable=self.extra_args_var, bg='#3e3e3e', fg='white', insertbackground='white', relief=tk.FLAT,
        ).grid(row=7, column=1, sticky=tk.EW, padx=10, pady=5, ipady=3)

    def update_texts(self) -> None:
        """Update localized texts."""
        self.legacy_ssl_check.config(text=_('Legacy SSL (Fix EOF)'))
        self.live_start_check.config(text=_('Live From Start'))
        self.part_files_check.config(text=_('Use .part files'))
        self.restrict_filenames_check.config(text=_('Restrict Filenames (ASCII)'))
        self.force_overwrite_check.config(text=_('Force Overwrite'))
        self.retries_label.config(text=_('Retries:'))
        self.wait_video_label.config(text=_('Wait for Video (seconds):'))
        self.extra_args_label.config(text=_('Extra Arguments (CLI):'))

    def get_data(self) -> Dict[str, Any]:
        """Collect tab data."""
        return {
            'legacy_ssl': self.legacy_ssl_var.get(),
            'live_start': self.live_start_var.get(),
            'part_files': self.part_files_var.get(),
            'restrict_filenames': self.restrict_filenames_var.get(),
            'force_overwrite': self.force_overwrite_var.get(),
            'retries': self.retries_var.get(),
            'wait_video': self.wait_video_var.get(),
            'extra_args': self.extra_args_var.get(),
        }
