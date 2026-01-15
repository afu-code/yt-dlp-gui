"""
Custom UI widgets for yt-dlp GUI.
Includes styled buttons with hover effects, placeholder entries, and tooltips.
"""

import tkinter as tk
from tkinter import ttk
from typing import Any, Optional


class ModernButton(tk.Button):
    """A styled primary button with hover effects."""

    def __init__(self, master: Optional[tk.Widget] = None, **kwargs: Any) -> None:
        self.default_bg = kwargs.get('bg', '#007acc')
        self.hover_bg = kwargs.get('activebackground', '#0094f0')
        
        defaults = {
            'relief': tk.FLAT,
            'bg': self.default_bg,
            'fg': 'white',
            'activebackground': self.hover_bg,
            'activeforeground': 'white',
            'font': ('Segoe UI', 10, 'bold'),
            'padx': 20,
            'pady': 10,
            'border': 0,
            'cursor': 'hand2',
        }
        defaults.update(kwargs)
        super().__init__(master, **defaults)
        
        self.bind('<Enter>', self._on_enter)
        self.bind('<Leave>', self._on_leave)

    def _on_enter(self, _: Any) -> None:
        self['background'] = self.hover_bg

    def _on_leave(self, _: Any) -> None:
        self['background'] = self.default_bg


class SecondaryButton(tk.Button):
    """A styled secondary button with hover effects."""

    def __init__(self, master: Optional[tk.Widget] = None, **kwargs: Any) -> None:
        self.default_bg = kwargs.get('bg', '#4e4e4e')
        self.hover_bg = kwargs.get('activebackground', '#606060')
        
        defaults = {
            'relief': tk.FLAT,
            'bg': self.default_bg,
            'fg': 'white',
            'activebackground': self.hover_bg,
            'activeforeground': 'white',
            'font': ('Segoe UI', 9),
            'padx': 15,
            'pady': 5,
            'border': 0,
            'cursor': 'hand2',
        }
        defaults.update(kwargs)
        super().__init__(master, **defaults)
        
        self.bind('<Enter>', self._on_enter)
        self.bind('<Leave>', self._on_leave)

    def _on_enter(self, _: Any) -> None:
        self['background'] = self.hover_bg

    def _on_leave(self, _: Any) -> None:
        self['background'] = self.default_bg


class PlaceholderEntry(tk.Entry):
    """An entry widget with placeholder text support."""

    def __init__(self, master: Any, placeholder: str = '', color: str = '#999999', **kwargs: Any) -> None:
        super().__init__(master, **kwargs)
        self.placeholder = placeholder
        self.placeholder_color = color
        self.default_fg = self['fg']

        self.bind('<FocusIn>', self._clear_placeholder)
        self.bind('<FocusOut>', self._add_placeholder)

        self._add_placeholder()

    def _clear_placeholder(self, _: Any) -> None:
        if self.get() == self.placeholder:
            self.delete(0, tk.END)
            self.config(fg=self.default_fg)

    def _add_placeholder(self, _: Any = None) -> None:
        if not self.get():
            self.insert(0, self.placeholder)
            self.config(fg=self.placeholder_color)


class Tooltip:
    """A simple tooltip widget for hover pointers."""

    def __init__(self, widget: tk.Widget, text: str) -> None:
        self.widget = widget
        self.text = text
        self.tip_window: Optional[tk.Toplevel] = None
        self.widget.bind('<Enter>', self.show_tip)
        self.widget.bind('<Leave>', self.hide_tip)

    def show_tip(self, _: Any) -> None:
        """Display text in tooltip window."""
        if self.tip_window or not self.text:
            return
        x, y, _, _ = self.widget.bbox('insert')
        x = x + self.widget.winfo_rootx() + 25
        y = y + self.widget.winfo_rooty() + 20
        self.tip_window = tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(True)
        tw.wm_geometry(f'+{x}+{y}')
        label = tk.Label(
            tw, text=self.text, justify=tk.LEFT,
            background='#ffffe0', relief=tk.SOLID, borderwidth=1,
            font=('tahoma', '8', 'normal'),
        )
        label.pack(ipadx=1)

    def hide_tip(self, _: Any) -> None:
        """Hide the tooltip window."""
        tw = self.tip_window
        self.tip_window = None
        if tw:
            tw.destroy()

