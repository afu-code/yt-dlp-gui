# -*- mode: python ; coding: utf-8 -*-

import os
import sys
from PyInstaller.utils.hooks import collect_data_files, collect_submodules

block_cipher = None

# Collect all locale files
locale_datas = collect_data_files('yt_dlp_gui.locales', include_py_files=False)

# Collect yt-dlp data files
ytdlp_datas = collect_data_files('yt_dlp', include_py_files=False)

# Combine all data files
datas = locale_datas + ytdlp_datas

# Collect all submodules
hiddenimports = collect_submodules('yt_dlp') + [
    'yt_dlp_gui',
    'yt_dlp_gui.app',
    'yt_dlp_gui.config',
    'yt_dlp_gui.logic',
    'yt_dlp_gui.settings',
    'yt_dlp_gui.widgets',
    'yt_dlp_gui.i18n',
    'yt_dlp_gui.logger',
    'yt_dlp_gui.tabs',
    'yt_dlp_gui.tabs.general',
    'yt_dlp_gui.tabs.network',
    'yt_dlp_gui.tabs.filters',
    'yt_dlp_gui.tabs.post',
    'yt_dlp_gui.tabs.advanced',
]

a = Analysis(
    ['yt_dlp_gui/main.py'],
    pathex=[],
    binaries=[],
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='yt-dlp-gui',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,  # Set to False for GUI application (no console window)
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=None,  # Add icon path here if you have one: 'icon.ico'
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='yt-dlp-gui',
)
