# Contributing to yt-dlp-gui

Thank you for your interest in contributing to yt-dlp-gui! We welcome contributions from everyone.

## How to Contribute

### Reporting Bugs

If you find a bug, please create an issue on GitHub with:
- A clear, descriptive title
- Steps to reproduce the issue
- Expected behavior
- Actual behavior
- Your environment (OS, Python version, yt-dlp version)
- Screenshots if applicable

### Suggesting Enhancements

We welcome feature requests! Please create an issue with:
- A clear, descriptive title
- Detailed description of the proposed feature
- Use cases and benefits
- Any relevant examples or mockups

### Pull Requests

1. **Fork the repository** and create your branch from `main`
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Set up your development environment**
   ```bash
   # Clone your fork
   git clone https://github.com/yourusername/yt-dlp-gui.git
   cd yt-dlp-gui
   
   # Install dependencies
   pip install -r requirements-dev.txt
   ```

3. **Make your changes**
   - Write clear, readable code
   - Follow the existing code style
   - Add comments where necessary
   - Update documentation if needed

4. **Test your changes**
   ```bash
   # Run tests
   pytest
   
   # Test the GUI
   python -m yt_dlp_gui.main
   ```

5. **Commit your changes**
   - Use clear, descriptive commit messages
   - Follow the format: `type: description`
   - Types: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`
   
   Example:
   ```bash
   git commit -m "feat: add dark theme support"
   ```

6. **Push to your fork and submit a pull request**
   ```bash
   git push origin feature/your-feature-name
   ```

7. **Wait for review**
   - Address any feedback from reviewers
   - Make requested changes if needed

## Development Guidelines

### Code Style

- Follow PEP 8 style guide
- Use meaningful variable and function names
- Keep functions focused and concise
- Add docstrings to classes and functions

### Internationalization (i18n)

When adding new UI text:

1. Use the `_()` function for all user-facing strings:
   ```python
   from .i18n import _
   label = tk.Label(text=_('Your Text Here'))
   ```

2. Add translations to locale files in `yt_dlp_gui/locales/`:
   - `zh_CN/LC_MESSAGES/yt_dlp_gui.po` (Chinese Simplified)
   - `zh_TW/LC_MESSAGES/yt_dlp_gui.po` (Chinese Traditional)
   - `ja/LC_MESSAGES/yt_dlp_gui.po` (Japanese)
   - `ko/LC_MESSAGES/yt_dlp_gui.po` (Korean)

3. Compile the translations:
   ```bash
   python -m yt_dlp_gui.compile_locales
   ```

### Testing

- Write tests for new features
- Ensure existing tests pass
- Test on multiple platforms if possible

### Documentation

- Update README.md if adding new features
- Update CHANGELOG.md following [Keep a Changelog](https://keepachangelog.com/)
- Add docstrings to new functions and classes

## Project Structure

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
�?  ├── logger.py        # Logging utilities
�?  ├── tabs/            # Tab implementations
�?  └── locales/         # Translation files
├── tests/               # Test files
├── README.md
├── CHANGELOG.md
├── CONTRIBUTING.md
├── LICENSE
└── pyproject.toml
```

## Questions?

If you have questions, feel free to:
- Open an issue for discussion
- Check existing issues and pull requests
- Read the documentation

Thank you for contributing! 🎉

