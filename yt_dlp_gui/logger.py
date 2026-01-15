"""
Logger implementation for yt-dlp GUI to capture and display progress/errors.
"""

import re
from typing import Any


class MyLogger:
    """
    Custom logger class that redirects yt-dlp log messages to the GUI's log area.
    """

    def __init__(self, gui: Any) -> None:
        """
        Initialize the logger.

        @param gui: Reference to the main YTDownloaderGUI instance
        """
        self.gui = gui
        self.ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')

    def strip_ansi(self, msg: str) -> str:
        """
        Remove ANSI escape sequences from a string.

        @param msg: The string possibly containing ANSI codes
        @return: Cleaned string
        """
        return self.ansi_escape.sub('', msg)

    def debug(self, msg: str) -> None:
        """Handle debug messages (mostly ignored in UI)."""
        pass

    def warning(self, msg: str) -> None:
        """Handle warning messages."""
        clean_msg = self.strip_ansi(msg)
        self.gui.root.after(0, lambda: self.gui.log(f'[WARN] {clean_msg}'))

    def error(self, msg: str) -> None:
        """Handle error messages."""
        clean_msg = self.strip_ansi(msg)
        self.gui.root.after(0, lambda: self.gui.log(f'[ERROR] {clean_msg}'))

    def info(self, msg: str) -> None:
        """Handle informational messages."""
        clean_msg = self.strip_ansi(msg)
        # yt-dlp sends a lot of info, we want to filter some or just show it
        # suppress the long download progress logs in the text area, since we have a progress bar
        if not clean_msg.startswith('[download] '):
            self.gui.root.after(0, lambda: self.gui.log(clean_msg))

