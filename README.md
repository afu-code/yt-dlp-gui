# yt-dlp-gui

[English](README.md) | [简体中文](README_zh.md)
<div align="center">

![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-Unlicense-green.svg)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey.svg)

A modern, user-friendly Graphical User Interface for [yt-dlp](https://github.com/yt-dlp/yt-dlp).

[Features](#features) �?[Installation](#installation) �?[Usage](#usage) �?[Screenshots](#screenshots) �?[Contributing](#contributing)

</div>

---

## �?Features

- 🎨 **Modern UI** - Clean, intuitive interface with dark theme support
- 🌍 **Multi-language** - Support for English, Chinese (Simplified/Traditional), Japanese, and Korean
- 📑 **Organized Settings** - Tabbed interface for easy configuration:
  - **General**: Format selection, quality settings, output templates
  - **Network**: Proxy configuration, cookies, rate limiting
  - **Filters**: Playlist filters, date ranges, file size limits
  - **Post-Processing**: Audio extraction, video conversion, metadata embedding
  - **Advanced**: Custom CLI arguments with real-time command preview
- ⚙️ **Settings Management** - Persistent configuration with GUI settings window
- 🔍 **FFmpeg Integration** - Automatic detection and configuration
- 📊 **Progress Tracking** - Real-time download progress and logging
- 🖥�?**Cross-platform** - Works on Windows, Linux, and macOS
- 🔄 **Easy Updates** - yt-dlp is a dependency, update via pip

## 📦 Installation

### Prerequisites

- Python 3.8 or higher
- FFmpeg (optional, but recommended for post-processing)

### Method 1: Install from PyPI (Recommended)

```bash
pip install yt-dlp-gui
```

### Method 2: Install from Source

```bash
# Clone the repository
git clone https://github.com/yourusername/yt-dlp-gui.git
cd yt-dlp-gui

# Install dependencies
pip install -r requirements.txt

# Or install in development mode
pip install -e .
```

### Installing FFmpeg

**Windows:**
- Download from [ffmpeg.org](https://ffmpeg.org/download.html)
- Or use [Chocolatey](https://chocolatey.org/): `choco install ffmpeg`

**Linux:**
```bash
# Ubuntu/Debian
sudo apt install ffmpeg

# Fedora
sudo dnf install ffmpeg

# Arch
sudo pacman -S ffmpeg
```

**macOS:**
```bash
brew install ffmpeg
```

## 🚀 Usage

### Running the GUI

**After installation:**
```bash
yt-dlp-gui
```

**From source:**

Windows:
```cmd
.\yt-dlp-gui.cmd
```

Linux/macOS:
```bash
./yt-dlp-gui.sh
```

Or directly with Python:
```bash
python -m yt_dlp_gui.main
```

### Basic Workflow

1. **Enter URL** - Paste a YouTube or supported site URL
2. **Configure Settings** - Choose format, quality, and other options via tabs
3. **Set Output** - Click Settings (�? to configure output directory and other preferences
4. **Download** - Click "START DOWNLOAD" and monitor progress

### Command Preview

The Advanced tab shows a real-time preview of the yt-dlp command that will be executed, helping you understand and verify your settings.

## 📸 Screenshots

<!-- Add screenshots here -->
```
Coming soon...
```

## 🛠�?Configuration

Settings are stored in `settings.json` in the application directory. You can configure:

- **Output Directory** - Where downloads are saved
- **FFmpeg Path** - Custom FFmpeg location
- **Language** - UI language preference
- **Theme** - UI theme selection
- **Proxy** - Network proxy settings
- **Cookies** - Browser cookies for authentication

## 🔧 Development

### Setting up Development Environment

```bash
# Clone the repository
git clone https://github.com/yourusername/yt-dlp-gui.git
cd yt-dlp-gui

# Install development dependencies
pip install -r requirements-dev.txt

# Run tests
pytest

# Run the application
python -m yt_dlp_gui.main
```

### Project Structure

```
yt-dlp-gui/
├── yt_dlp_gui/           # Main package
�?  ├── __init__.py
�?  ├── main.py          # Entry point
�?  ├── app.py           # Main GUI class
�?  ├── config.py        # Configuration management
�?  ├── logic.py         # Business logic
�?  ├── settings.py      # Settings window
�?  ├── widgets.py       # Custom widgets
�?  ├── i18n.py          # Internationalization
�?  ├── tabs/            # Tab implementations
�?  └── locales/         # Translation files
├── tests/               # Test files
├── README.md
├── CHANGELOG.md
├── CONTRIBUTING.md
└── pyproject.toml
```

### Adding Translations

1. Edit `.po` files in `yt_dlp_gui/locales/[language]/LC_MESSAGES/`
2. Compile translations:
   ```bash
   python -m yt_dlp_gui.compile_locales
   ```

See [CONTRIBUTING.md](CONTRIBUTING.md) for more details.

## 🤝 Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Ways to Contribute

- 🐛 Report bugs
- 💡 Suggest new features
- 🌍 Add or improve translations
- 📝 Improve documentation
- 🔧 Submit pull requests

## 📝 License

This project is released into the public domain under the [Unlicense](LICENSE).

## 🙏 Acknowledgments

- [yt-dlp](https://github.com/yt-dlp/yt-dlp) - The powerful command-line tool this GUI is built upon
- All contributors and users of this project

## 📮 Support

- **Issues**: [GitHub Issues](https://github.com/yourusername/yt-dlp-gui/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/yt-dlp-gui/discussions)

## ⚠️ Disclaimer

This tool is for personal use only. Please respect copyright laws and the terms of service of the websites you download from.

---

<div align="center">
Made with ❤️ by the community
</div>

