# Quick Start Guide

## For Users

### Installation

```bash
pip install yt-dlp-gui
```

### Run

```bash
yt-dlp-gui
```

That's it! The GUI will open and you can start downloading.

## For Developers

### Setup

```bash
# Clone
git clone https://github.com/yourusername/yt-dlp-gui.git
cd yt-dlp-gui

# Install
pip install -r requirements-dev.txt

# Run
python -m yt_dlp_gui.main
```

### Before Committing

```bash
# Format code
black yt_dlp_gui/

# Run tests
pytest

# Check linting
flake8 yt_dlp_gui/
```

### Building

```bash
# Build package
python -m build

# Install locally
pip install dist/yt_dlp_gui-*.whl
```

## Common Tasks

### Update yt-dlp

```bash
pip install --upgrade yt-dlp
```

### Update yt-dlp-gui

```bash
pip install --upgrade yt-dlp-gui
```

### Compile Translations

```bash
python -m yt_dlp_gui.compile_locales
```

## Troubleshooting

### FFmpeg not found

Install FFmpeg and add it to your PATH, or set the path in Settings.

### Permission errors

Run with appropriate permissions or change the output directory.

### Import errors

Make sure all dependencies are installed:
```bash
pip install -r requirements.txt
```

For more details, see the full [README.md](README.md).

