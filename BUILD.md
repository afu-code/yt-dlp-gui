# Building with PyInstaller

This guide explains how to build a standalone executable of yt-dlp-gui using PyInstaller.

## Prerequisites

1. **Install PyInstaller**
   ```bash
   pip install pyinstaller
   ```

2. **Install all dependencies**
   ```bash
   pip install -r requirements.txt
   pip install -r requirements-dev.txt
   ```

## Building

### Windows

Run the build script:
```cmd
build.cmd
```

Or manually:
```cmd
pyinstaller --clean yt-dlp-gui.spec
```

### Linux/macOS

Run the build script:
```bash
chmod +x build.sh
./build.sh
```

Or manually:
```bash
pyinstaller --clean yt-dlp-gui.spec
```

## Output

The executable will be created in:
```
dist/yt-dlp-gui/
```

### Windows
- `dist/yt-dlp-gui/yt-dlp-gui.exe`

### Linux/macOS
- `dist/yt-dlp-gui/yt-dlp-gui`

## Distribution

To distribute the application:

1. **Zip the entire folder**
   ```bash
   # Windows
   Compress-Archive -Path dist\yt-dlp-gui -DestinationPath yt-dlp-gui-windows.zip
   
   # Linux/macOS
   cd dist
   tar -czf yt-dlp-gui-linux.tar.gz yt-dlp-gui/
   ```

2. **Share the zip file** with users

Users can extract and run the executable without installing Python or any dependencies.

## Customization

### Adding an Icon

1. Create or obtain an `.ico` file (Windows) or `.icns` file (macOS)
2. Edit `yt-dlp-gui.spec`:
   ```python
   exe = EXE(
       ...
       icon='path/to/icon.ico',  # Add this line
       ...
   )
   ```

### One-File Build

To create a single executable file instead of a folder:

Edit `yt-dlp-gui.spec`:
```python
exe = EXE(
    pyz,
    a.scripts,
    a.binaries,      # Add these
    a.zipfiles,      # Add these
    a.datas,         # Add these
    [],
    name='yt-dlp-gui',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    icon=None,
)

# Remove or comment out the COLLECT section
```

Then rebuild:
```bash
pyinstaller --clean yt-dlp-gui.spec
```

The single executable will be in `dist/yt-dlp-gui.exe` (Windows) or `dist/yt-dlp-gui` (Linux/macOS).

## Troubleshooting

### Missing Modules

If you get import errors when running the executable:

1. Add the missing module to `hiddenimports` in `yt-dlp-gui.spec`:
   ```python
   hiddenimports = [
       'missing_module_name',
       ...
   ]
   ```

2. Rebuild

### Missing Data Files

If locale files or other data are missing:

1. Check the `datas` section in `yt-dlp-gui.spec`
2. Add missing files:
   ```python
   datas = [
       ('path/to/data', 'destination/in/exe'),
       ...
   ]
   ```

3. Rebuild

### Large File Size

The executable may be large (100-200 MB) because it includes:
- Python interpreter
- All dependencies (yt-dlp, etc.)
- Locale files

To reduce size:
- Use UPX compression (already enabled)
- Exclude unnecessary modules
- Use one-file mode with compression

### Antivirus False Positives

Some antivirus software may flag PyInstaller executables as suspicious. This is a known issue with PyInstaller.

Solutions:
- Sign the executable with a code signing certificate
- Submit the executable to antivirus vendors for whitelisting
- Inform users this is a false positive

## Testing

Before distributing:

1. **Test on a clean system** without Python installed
2. **Test all features**:
   - Download a video
   - Change settings
   - Switch languages
   - Use different formats

3. **Test on different OS versions**:
   - Windows 10, 11
   - Ubuntu 20.04, 22.04
   - macOS 11+

## Automated Builds

For automated builds with GitHub Actions, see `.github/workflows/build.yml` (if available).

## Notes

- The executable is platform-specific (Windows .exe won't run on Linux)
- Build on each target platform for best compatibility
- FFmpeg is NOT included - users need to install it separately
- The executable size is normal for PyInstaller applications

## Support

If you encounter issues:
1. Check the PyInstaller documentation: https://pyinstaller.org/
2. Open an issue on GitHub with build logs
3. Include your OS and Python version
