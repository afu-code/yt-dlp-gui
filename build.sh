#!/usr/bin/env bash
# Build script for Linux/macOS using PyInstaller

echo "Building yt-dlp-gui..."
echo ""

# Clean previous builds
rm -rf build dist

# Run PyInstaller
pyinstaller --clean yt-dlp-gui.spec

if [ $? -eq 0 ]; then
    echo ""
    echo "Build successful!"
    echo "Executable is in: dist/yt-dlp-gui/"
    echo ""
else
    echo ""
    echo "Build failed!"
    echo ""
    exit 1
fi
