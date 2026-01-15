"""
Post-processing settings tab for yt-dlp GUI.
"""

import tkinter as tk
from tkinter import ttk
from typing import Any, Dict

from ..i18n import _


class PostTab(ttk.Frame):
    """
    Tab for embedding metadata, thumbnails, and other post-processing options.
    """

    def __init__(self, master: ttk.Notebook, **kwargs: Any) -> None:
        """
        Initialize the Post Processing tab.
        """
        super().__init__(master, **kwargs)
        self.pack(fill=tk.BOTH, expand=True)

        frame = ttk.Frame(self, padding=20)
        frame.pack(fill=tk.BOTH, expand=True)
        frame.columnconfigure(1, weight=1)

        # Embeds
        self.embed_meta_var = tk.BooleanVar(value=True)
        self.embed_meta_check = ttk.Checkbutton(frame, text=_('Embed Metadata'), variable=self.embed_meta_var)
        self.embed_meta_check.grid(row=0, column=0, sticky=tk.W, pady=5)

        self.embed_thumbnail_var = tk.BooleanVar(value=True)
        self.embed_thumbnail_check = ttk.Checkbutton(frame, text=_('Embed Thumbnail'), variable=self.embed_thumbnail_var)
        self.embed_thumbnail_check.grid(row=0, column=1, sticky=tk.W, pady=5)

        self.embed_subs_var = tk.BooleanVar()
        self.embed_subs_check = ttk.Checkbutton(frame, text=_('Embed Subtitles'), variable=self.embed_subs_var)
        self.embed_subs_check.grid(row=1, column=0, sticky=tk.W, pady=5)

        self.embed_chapters_var = tk.BooleanVar(value=True)
        self.embed_chapters_check = ttk.Checkbutton(frame, text=_('Embed Chapters'), variable=self.embed_chapters_var)
        self.embed_chapters_check.grid(row=1, column=1, sticky=tk.W, pady=5)

        # Subtitle langs
        self.sub_langs_label = ttk.Label(frame, text=_('Subtitle Languages (e.g. en,zh):'))
        self.sub_langs_label.grid(row=2, column=0, sticky=tk.W, pady=5)
        self.sub_langs_var = tk.StringVar(value='en,zh.*')
        tk.Entry(
            frame, textvariable=self.sub_langs_var, bg='#3e3e3e', fg='white', insertbackground='white', relief=tk.FLAT,
        ).grid(row=2, column=1, sticky=tk.EW, padx=10, pady=5, ipady=3)

        # SponsorBlock
        self.sponsorblock_label = ttk.Label(frame, text=_('SponsorBlock (e.g. all):'))
        self.sponsorblock_label.grid(row=3, column=0, sticky=tk.W, pady=5)
        self.sponsorblock_var = tk.StringVar()
        tk.Entry(
            frame, textvariable=self.sponsorblock_var, bg='#3e3e3e', fg='white', insertbackground='white',
            relief=tk.FLAT,
        ).grid(row=3, column=1, sticky=tk.EW, padx=10, pady=5, ipady=3)

        ttk.Separator(frame, orient=tk.HORIZONTAL).grid(row=4, column=0, columnspan=2, sticky=tk.EW, pady=15)

        # Write Files
        self.write_desc_var = tk.BooleanVar()
        self.write_desc_check = ttk.Checkbutton(frame, text=_('Write Description'), variable=self.write_desc_var)
        self.write_desc_check.grid(row=5, column=0, sticky=tk.W, pady=5)

        self.write_info_var = tk.BooleanVar()
        self.write_info_check = ttk.Checkbutton(frame, text=_('Write Info JSON'), variable=self.write_info_var)
        self.write_info_check.grid(row=5, column=1, sticky=tk.W, pady=5)

        self.write_thumbnail_disk_var = tk.BooleanVar()
        self.write_thumbnail_disk_check = ttk.Checkbutton(
            frame, text=_('Save Thumbnail to Disk'), variable=self.write_thumbnail_disk_var,
        )
        self.write_thumbnail_disk_check.grid(row=6, column=0, sticky=tk.W, pady=5)

    def update_texts(self) -> None:
        """Update localized texts."""
        self.embed_meta_check.config(text=_('Embed Metadata'))
        self.embed_thumbnail_check.config(text=_('Embed Thumbnail'))
        self.embed_subs_check.config(text=_('Embed Subtitles'))
        self.embed_chapters_check.config(text=_('Embed Chapters'))
        self.sub_langs_label.config(text=_('Subtitle Languages (e.g. en,zh):'))
        self.sponsorblock_label.config(text=_('SponsorBlock (e.g. all):'))
        self.write_desc_check.config(text=_('Write Description'))
        self.write_info_check.config(text=_('Write Info JSON'))
        self.write_thumbnail_disk_check.config(text=_('Save Thumbnail to Disk'))

    def get_data(self) -> Dict[str, Any]:
        """Collect tab data."""
        return {
            'embed_metadata': self.embed_meta_var.get(),
            'embed_thumbnail': self.embed_thumbnail_var.get(),
            'embed_subs': self.embed_subs_var.get(),
            'embed_chapters': self.embed_chapters_var.get(),
            'sub_langs': self.sub_langs_var.get(),
            'sponsorblock': self.sponsorblock_var.get(),
            'write_desc': self.write_desc_var.get(),
            'write_info': self.write_info_var.get(),
            'write_thumbnail_disk': self.write_thumbnail_disk_var.get(),
        }
