"""
Tabs for yt-dlp GUI.
"""

from .advanced import AdvancedTab
from .filters import FiltersTab
from .general import GeneralTab
from .network import NetworkTab
from .post import PostTab

__all__ = ['GeneralTab', 'NetworkTab', 'FiltersTab', 'PostTab', 'AdvancedTab']
