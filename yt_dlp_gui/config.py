"""
Configuration management for yt-dlp GUI.
Aligns with yt-dlp core's Config utility for robust settings management.
"""

import json
import os
from typing import Any, Dict

from yt_dlp.utils import expand_path

CONFIG_NAME = 'yt-dlp-gui.json'


def get_config_path() -> str:
    """
    Get the absolute path to the GUI configuration file.
    Prefers the same directory as the script (Portable mode).

    @return: Absolute path to the config file
    """
    base_dir = os.path.dirname(os.path.abspath(__file__))
    portable_path = os.path.join(os.path.dirname(os.path.dirname(base_dir)), CONFIG_NAME)
    
    return portable_path


def load_config() -> Dict[str, Any]:
    """
    Load configuration settings from the default config file.
    Includes default fallback values.

    @return: Dictionary containing configuration settings
    """
    default_config: Dict[str, Any] = {
        'output_dir': os.getcwd(),
        'cookies_path': '',
        'data_sync_id': '',
        'proxy_url': '',
        'language': 'en',
        'theme': 'dark',
    }

    config_path = get_config_path()
    
    if os.path.exists(config_path):
        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                saved_config = json.load(f)
                # Only update keys that we recognize to avoid pollution
                for k, v in saved_config.items():
                    if k in default_config:
                        default_config[k] = v
        except Exception as e:
            print(f'Error loading config: {e}')

    # Sanitize paths
    if default_config['output_dir']:
        default_config['output_dir'] = expand_path(default_config['output_dir'])
    if default_config['cookies_path']:
        default_config['cookies_path'] = expand_path(default_config['cookies_path'])

    return default_config


def save_config(config: Dict[str, Any]) -> None:
    """
    Save configuration settings to the default config file.

    @param config: Dictionary containing configuration to save
    """
    config_path = get_config_path()
    try:
        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(config_path), exist_ok=True)
        
        with open(config_path, 'w', encoding='utf-8') as f:
            json.dump(config, f, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f'Error saving config: {e}')

