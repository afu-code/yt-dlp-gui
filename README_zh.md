# yt-dlp-gui

[English](README.md) | [简体中文](README_zh.md)
<div align="center">

![Python 版本](https://img.shields.io/badge/python-3.8+-blue.svg)
![许可证](https://img.shields.io/badge/license-Unlicense-green.svg)
![平台](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey.svg)

[yt-dlp](https://github.com/yt-dlp/yt-dlp) 的现代化、用户友好的图形界面�?

[功能特性](#-功能特�? �?[安装](#-安装) �?[使用](#-使用) �?[截图](#-截图) �?[贡献](#-贡献)

</div>

---

## �?功能特�?

- 🎨 **现代化界�?* - 简洁直观的界面，支持深色主�?
- 🌍 **多语言支持** - 支持英语、简体中文、繁体中文、日语和韩语
- 📑 **分类设置** - 标签页式界面，便于配置：
  - **通用**：格式选择、质量设置、输出模�?
  - **网络**：代理配置、Cookie、速率限制
  - **过滤�?*：播放列表过滤、日期范围、文件大小限�?
  - **后处�?*：音频提取、视频转换、元数据嵌入
  - **高级**：自定义 CLI 参数，实时命令预�?
- ⚙️ **设置管理** - 持久化配置，带有 GUI 设置窗口
- 🔍 **FFmpeg 集成** - 自动检测和配置
- 📊 **进度跟踪** - 实时下载进度和日志记�?
- 🖥�?**跨平�?* - 支持 Windows、Linux �?macOS
- 🔄 **轻松更新** - yt-dlp 作为依赖项，通过 pip 更新

## 📦 安装

### 前置要求

- Python 3.8 或更高版�?
- FFmpeg（可选，但推荐用于后处理�?

### 方法 1：从 PyPI 安装（推荐）

```bash
pip install yt-dlp-gui
```

### 方法 2：从源码安装

```bash
# 克隆仓库
git clone https://github.com/yourusername/yt-dlp-gui.git
cd yt-dlp-gui

# 安装依赖
pip install -r requirements.txt

# 或以开发模式安�?
pip install -e .
```

### 安装 FFmpeg

**Windows:**
- �?[ffmpeg.org](https://ffmpeg.org/download.html) 下载
- 或使�?[Chocolatey](https://chocolatey.org/)：`choco install ffmpeg`

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

## 🚀 使用

### 运行 GUI

**安装后：**
```bash
yt-dlp-gui
```

**从源码运行：**

Windows:
```cmd
.\yt-dlp-gui.cmd
```

Linux/macOS:
```bash
./yt-dlp-gui.sh
```

或直接使�?Python�?
```bash
python -m yt_dlp_gui.main
```

### 基本工作流程

1. **输入 URL** - 粘贴 YouTube 或其他支持网站的 URL
2. **配置设置** - 通过标签页选择格式、质量和其他选项
3. **设置输出** - 点击设置（⚙）配置输出目录和其他首选项
4. **下载** - 点击"开始下�?并监控进�?

### 命令预览

高级标签页显示将要执行的 yt-dlp 命令的实时预览，帮助您理解和验证设置�?

## 📸 截图

<!-- 在此添加截图 -->
```
即将推出...
```

## 🛠�?配置

设置存储在应用程序目录的 `settings.json` 中。您可以配置�?

- **输出目录** - 下载文件的保存位�?
- **FFmpeg 路径** - 自定�?FFmpeg 位置
- **语言** - UI 语言偏好
- **主题** - UI 主题选择
- **代理** - 网络代理设置
- **Cookies** - 用于身份验证的浏览器 Cookie

## 🔧 开�?

### 设置开发环�?

```bash
# 克隆仓库
git clone https://github.com/yourusername/yt-dlp-gui.git
cd yt-dlp-gui

# 安装开发依�?
pip install -r requirements-dev.txt

# 运行测试
pytest

# 运行应用程序
python -m yt_dlp_gui.main
```

### 项目结构

```
yt-dlp-gui/
├── yt_dlp_gui/           # 主包
�?  ├── __init__.py
�?  ├── main.py          # 入口�?
�?  ├── app.py           # �?GUI �?
�?  ├── config.py        # 配置管理
�?  ├── logic.py         # 业务逻辑
�?  ├── settings.py      # 设置窗口
�?  ├── widgets.py       # 自定义小部件
�?  ├── i18n.py          # 国际�?
�?  ├── tabs/            # 标签页实�?
�?  └── locales/         # 翻译文件
├── tests/               # 测试文件
├── README.md
├── CHANGELOG.md
├── CONTRIBUTING.md
└── pyproject.toml
```

### 添加翻译

1. 编辑 `yt_dlp_gui/locales/[语言]/LC_MESSAGES/` 中的 `.po` 文件
2. 编译翻译�?
   ```bash
   python -m yt_dlp_gui.compile_locales
   ```

详见 [CONTRIBUTING.md](CONTRIBUTING.md)�?

## 🤝 贡献

欢迎贡献！请阅读 [CONTRIBUTING.md](CONTRIBUTING.md) 了解指南�?

### 贡献方式

- 🐛 报告错误
- 💡 建议新功�?
- 🌍 添加或改进翻�?
- 📝 改进文档
- 🔧 提交拉取请求

## 📝 许可�?

本项目在 [Unlicense](LICENSE) 下发布到公共领域�?

## 🙏 致谢

- [yt-dlp](https://github.com/yt-dlp/yt-dlp) - �?GUI 基于的强大命令行工具
- 本项目的所有贡献者和用户

## 📮 支持

- **问题**：[GitHub Issues](https://github.com/yourusername/yt-dlp-gui/issues)
- **讨论**：[GitHub Discussions](https://github.com/yourusername/yt-dlp-gui/discussions)

## ⚠️ 免责声明

此工具仅供个人使用。请尊重版权法和您下载网站的服务条款�?

---

<div align="center">
由社区用 ❤️ 制作
</div>

