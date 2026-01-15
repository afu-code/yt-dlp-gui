"""
PyInstaller hook for yt_dlp_gui package.
Ensures all necessary data files and modules are included.
"""

from PyInstaller.utils.hooks import collect_data_files, collect_submodules

# Collect all locale files
datas = collect_data_files('yt_dlp_gui', subdir='locales', include_py_files=False)

# Collect all submodules
hiddenimports = collect_submodules('yt_dlp_gui')
