"""
Basic tests for the yt-dlp-gui application.
"""

import pytest
from yt_dlp_gui.config import load_config, save_config
from yt_dlp_gui.i18n import set_language, _


class TestConfig:
    """Test configuration management."""

    def test_load_config_default(self, tmp_path, monkeypatch):
        """Test loading default configuration."""
        # Change to temp directory
        monkeypatch.chdir(tmp_path)
        
        config = load_config()
        assert isinstance(config, dict)
        assert 'language' in config
        assert 'theme' in config

    def test_save_and_load_config(self, tmp_path, monkeypatch):
        """Test saving and loading configuration."""
        monkeypatch.chdir(tmp_path)
        
        test_config = {
            'language': 'zh_CN',
            'theme': 'dark',
            'output_dir': '/test/path',
        }
        
        save_config(test_config)
        loaded_config = load_config()
        
        assert loaded_config['language'] == 'zh_CN'
        assert loaded_config['theme'] == 'dark'
        assert loaded_config['output_dir'] == '/test/path'


class TestI18n:
    """Test internationalization."""

    def test_set_language_english(self):
        """Test setting English language."""
        set_language('en')
        # Test a common translation
        result = _('Ready')
        assert isinstance(result, str)

    def test_set_language_chinese(self):
        """Test setting Chinese language."""
        set_language('zh_CN')
        result = _('Ready')
        assert isinstance(result, str)

    def test_translation_fallback(self):
        """Test that missing translations fall back to English."""
        set_language('en')
        # Non-existent key should return the key itself
        result = _('NonExistentKey123')
        assert result == 'NonExistentKey123'


class TestLogic:
    """Test business logic functions."""

    def test_build_ydl_opts_basic(self):
        """Test building basic yt-dlp options."""
        from yt_dlp_gui.logic import build_ydl_opts
        
        ui_data = {
            'output_dir': '/test',
            'format_id': 'best',
            'video_url': 'https://www.youtube.com/watch?v=test',
        }
        
        # Create a mock GUI object
        class MockGUI:
            def progress_hook(self, d):
                pass
        
        mock_gui = MockGUI()
        opts = build_ydl_opts(ui_data, mock_gui)
        
        assert isinstance(opts, dict)
        assert 'outtmpl' in opts
        assert 'progress_hooks' in opts

    def test_get_command_preview(self):
        """Test command preview generation."""
        from yt_dlp_gui.logic import get_command_preview
        
        ui_data = {
            'output_dir': '/test',
            'format_id': 'best',
            'video_url': 'https://www.youtube.com/watch?v=test',
        }
        
        preview = get_command_preview(ui_data)
        
        assert isinstance(preview, str)
        assert 'yt-dlp' in preview
        assert 'https://www.youtube.com/watch?v=test' in preview


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
