"""
Filters settings tab for yt-dlp GUI.
"""

import tkinter as tk
from tkinter import ttk
from typing import Any, Dict

from ..i18n import _


class FiltersTab(ttk.Frame):
    """
    Tab for playlist items and metadata filtering.
    """

    def __init__(self, master: ttk.Notebook, **kwargs: Any) -> None:
        """
        Initialize the Filters tab.
        """
        super().__init__(master, **kwargs)
        self.pack(fill=tk.BOTH, expand=True)

        frame = ttk.Frame(self, padding=20)
        frame.pack(fill=tk.BOTH, expand=True)
        frame.columnconfigure(1, weight=1)

        # Playlist Items
        self.playlist_items_label = ttk.Label(frame, text=_('Playlist Items (e.g. 1,2,5-10):'))
        self.playlist_items_label.grid(row=0, column=0, sticky=tk.W, pady=5)
        self.playlist_items_var = tk.StringVar()
        tk.Entry(
            frame, textvariable=self.playlist_items_var, bg='#3e3e3e', fg='white', insertbackground='white',
            relief=tk.FLAT,
        ).grid(row=0, column=1, sticky=tk.EW, padx=10, pady=5, ipady=3)

        # Date Filters
        self.date_label = ttk.Label(frame, text=_('Date (YYYYMMDD):'))
        self.date_label.grid(row=1, column=0, sticky=tk.W, pady=5)
        self.date_var = tk.StringVar()
        tk.Entry(
            frame, textvariable=self.date_var, bg='#3e3e3e', fg='white', insertbackground='white', relief=tk.FLAT,
        ).grid(row=1, column=1, sticky=tk.EW, padx=10, pady=5, ipady=3)

        self.datebefore_label = ttk.Label(frame, text=_('Date Before:'))
        self.datebefore_label.grid(row=2, column=0, sticky=tk.W, pady=5)
        self.datebefore_var = tk.StringVar()
        tk.Entry(
            frame, textvariable=self.datebefore_var, bg='#3e3e3e', fg='white', insertbackground='white', relief=tk.FLAT,
        ).grid(row=2, column=1, sticky=tk.EW, padx=10, pady=5, ipady=3)

        self.dateafter_label = ttk.Label(frame, text=_('Date After:'))
        self.dateafter_label.grid(row=3, column=0, sticky=tk.W, pady=5)
        self.dateafter_var = tk.StringVar()
        tk.Entry(
            frame, textvariable=self.dateafter_var, bg='#3e3e3e', fg='white', insertbackground='white', relief=tk.FLAT,
        ).grid(row=3, column=1, sticky=tk.EW, padx=10, pady=5, ipady=3)

        # Filesize Filters
        self.min_filesize_label = ttk.Label(frame, text=_('Min Filesize (e.g. 50k):'))
        self.min_filesize_label.grid(row=4, column=0, sticky=tk.W, pady=5)
        self.min_filesize_var = tk.StringVar()
        tk.Entry(
            frame, textvariable=self.min_filesize_var, bg='#3e3e3e', fg='white', insertbackground='white',
            relief=tk.FLAT,
        ).grid(row=4, column=1, sticky=tk.EW, padx=10, pady=5, ipady=3)

        self.max_filesize_label = ttk.Label(frame, text=_('Max Filesize (e.g. 50m):'))
        self.max_filesize_label.grid(row=5, column=0, sticky=tk.W, pady=5)
        self.max_filesize_var = tk.StringVar()
        tk.Entry(
            frame, textvariable=self.max_filesize_var, bg='#3e3e3e', fg='white', insertbackground='white',
            relief=tk.FLAT,
        ).grid(row=5, column=1, sticky=tk.EW, padx=10, pady=5, ipady=3)

        # Match Filters
        self.match_filter_label = ttk.Label(frame, text=_('Match Filter:'))
        self.match_filter_label.grid(row=6, column=0, sticky=tk.W, pady=5)
        self.match_filter_var = tk.StringVar()
        tk.Entry(
            frame, textvariable=self.match_filter_var, bg='#3e3e3e', fg='white', insertbackground='white',
            relief=tk.FLAT,
        ).grid(row=6, column=1, sticky=tk.EW, padx=10, pady=5, ipady=3)

    def update_texts(self) -> None:
        """Update localized texts."""
        self.playlist_items_label.config(text=_('Playlist Items (e.g. 1,2,5-10):'))
        self.date_label.config(text=_('Date (YYYYMMDD):'))
        self.datebefore_label.config(text=_('Date Before:'))
        self.dateafter_label.config(text=_('Date After:'))
        self.min_filesize_label.config(text=_('Min Filesize (e.g. 50k):'))
        self.max_filesize_label.config(text=_('Max Filesize (e.g. 50m):'))
        self.match_filter_label.config(text=_('Match Filter:'))

    def get_data(self) -> Dict[str, Any]:
        """Collect tab data."""
        return {
            'playlist_items': self.playlist_items_var.get(),
            'date': self.date_var.get(),
            'datebefore': self.datebefore_var.get(),
            'dateafter': self.dateafter_var.get(),
            'min_filesize': self.min_filesize_var.get(),
            'max_filesize': self.max_filesize_var.get(),
            'match_filter': self.match_filter_var.get(),
        }
