"""
Network settings tab for yt-dlp GUI.
"""

import tkinter as tk
from tkinter import ttk
from typing import Any, Dict

from ..i18n import _


class NetworkTab(ttk.Frame):
    """
    Tab for network and proxy settings.
    """

    def __init__(self, master: ttk.Notebook, **kwargs: Any) -> None:
        """
        Initialize the Network tab.
        """
        super().__init__(master, **kwargs)
        self.pack(fill=tk.BOTH, expand=True)

        frame = ttk.Frame(self, padding=20)
        frame.pack(fill=tk.BOTH, expand=True)
        frame.columnconfigure(1, weight=1)

        # Browser Cookies
        self.browser_cookies_label = ttk.Label(frame, text=_('Browser Cookies:'))
        self.browser_cookies_label.grid(row=0, column=0, sticky=tk.W, pady=5)
        self.browser_var = tk.StringVar(value='none')
        browsers = ['none', 'chrome', 'firefox', 'edge', 'opera', 'brave', 'vivaldi', 'safari']
        ttk.Combobox(
            frame, textvariable=self.browser_var, values=browsers, state='readonly',
        ).grid(row=0, column=1, sticky=tk.EW, padx=10, pady=5)

        # User Agent
        self.user_agent_label = ttk.Label(frame, text=_('User Agent:'))
        self.user_agent_label.grid(row=1, column=0, sticky=tk.W, pady=5)
        self.user_agent_var = tk.StringVar()
        tk.Entry(
            frame, textvariable=self.user_agent_var, bg='#3e3e3e', fg='white', insertbackground='white', relief=tk.FLAT,
        ).grid(row=1, column=1, sticky=tk.EW, padx=10, pady=5, ipady=3)

        # Rate Limit
        self.limit_rate_label = ttk.Label(frame, text=_('Rate Limit (e.g. 5M):'))
        self.limit_rate_label.grid(row=2, column=0, sticky=tk.W, pady=5)
        self.rate_limit_var = tk.StringVar()
        tk.Entry(
            frame, textvariable=self.rate_limit_var, bg='#3e3e3e', fg='white', insertbackground='white', relief=tk.FLAT,
        ).grid(row=2, column=1, sticky=tk.EW, padx=10, pady=5, ipady=3)

        # Socket Timeout
        self.timeout_label = ttk.Label(frame, text=_('Socket Timeout (s):'))
        self.timeout_label.grid(row=3, column=0, sticky=tk.W, pady=5)
        self.timeout_var = tk.StringVar()
        tk.Entry(
            frame, textvariable=self.timeout_var, bg='#3e3e3e', fg='white', insertbackground='white', relief=tk.FLAT,
        ).grid(row=3, column=1, sticky=tk.EW, padx=10, pady=5, ipady=3)

        # Source IP
        self.source_address_label = ttk.Label(frame, text=_('Source IP:'))
        self.source_address_label.grid(row=4, column=0, sticky=tk.W, pady=5)
        self.source_ip_var = tk.StringVar()
        tk.Entry(
            frame, textvariable=self.source_ip_var, bg='#3e3e3e', fg='white', insertbackground='white', relief=tk.FLAT,
        ).grid(row=4, column=1, sticky=tk.EW, padx=10, pady=5, ipady=3)

        # Proxy
        self.proxy_label = ttk.Label(frame, text=_('Proxy URL:'))
        self.proxy_label.grid(row=5, column=0, sticky=tk.W, pady=5)
        self.proxy_override_var = tk.StringVar()
        tk.Entry(
            frame, textvariable=self.proxy_override_var, bg='#3e3e3e', fg='white',
            insertbackground='white', relief=tk.FLAT,
        ).grid(row=5, column=1, sticky=tk.EW, padx=10, pady=5, ipady=3)

    def update_texts(self) -> None:
        """Update localized texts."""
        self.browser_cookies_label.config(text=_('Browser Cookies:'))
        self.user_agent_label.config(text=_('User Agent:'))
        self.limit_rate_label.config(text=_('Rate Limit (e.g. 5M):'))
        self.timeout_label.config(text=_('Socket Timeout (s):'))
        self.source_address_label.config(text=_('Source IP:'))
        self.proxy_label.config(text=_('Proxy URL:'))

    def get_data(self) -> Dict[str, Any]:
        """Collect tab data."""
        return {
            'browser': self.browser_var.get(),
            'user_agent': self.user_agent_var.get(),
            'rate_limit': self.rate_limit_var.get(),
            'timeout': self.timeout_var.get(),
            'source_ip': self.source_ip_var.get(),
            'proxy_override': self.proxy_override_var.get(),
        }
