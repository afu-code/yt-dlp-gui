"""
Standard i18n support for yt-dlp GUI using gettext.
"""

import gettext
import os
import locale
from typing import Optional, Dict

# Define available languages
LANGUAGES: Dict[str, str] = {
    'en': 'English',
    'zh': '简体中文',
    'zh_TW': '繁體中文',
    'ja': '日本語',
    'ko': '한국어',
}

DOMAIN = 'yt_dlp_gui'
LOCALES_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'locales')

# Current translation object
_t = gettext.NullTranslations()

def set_language(lang: str):
    """
    Set the current language for the application.
    @param lang: Language code (e.g. 'zh_CN', 'en')
    """
    global _t
    
    # Map short codes to standard gettext codes if necessary
    lang_map = {
        'zh': 'zh_CN',
        'zh_TW': 'zh_TW',
        'ja': 'ja',
        'ko': 'ko',
        'en': 'en',
    }
    target_lang = lang_map.get(lang, lang)
    
    try:
        _t = gettext.translation(DOMAIN, LOCALES_DIR, languages=[target_lang])
    except (OSError, IOError):
        # Fallback to default (NullTranslations returns the string itself)
        _t = gettext.NullTranslations()

def _(message: str) -> str:
    """Translate the message."""
    return _t.gettext(message)

# Initialize with system language or English
try:
    set_language('en')
except Exception:
    pass
