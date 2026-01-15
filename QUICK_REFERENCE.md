# 快速参考

## 运行程序

### 开发模式
```bash
# Windows
.\yt-dlp-gui.cmd

# Linux/macOS  
./yt-dlp-gui.sh

# 或
python -m yt_dlp_gui.main
```

## 构建可执行文件

### 1. 安装 PyInstaller
```bash
pip install pyinstaller
```

### 2. 构建
```bash
# Windows
build.cmd

# Linux/macOS
chmod +x build.sh
./build.sh
```

### 3. 输出位置
```
dist/yt-dlp-gui/
```

## 重要文件

| 文件 | 用途 |
|------|------|
| `yt-dlp-gui.spec` | PyInstaller 配置 |
| `build.cmd` | Windows 构建脚本 |
| `build.sh` | Linux/macOS 构建脚本 |
| `BUILD.md` | 详细构建指南（英文） |
| `BUILD_zh.md` | 详细构建指南（中文） |
| `hooks/hook-yt_dlp_gui.py` | PyInstaller hook |

## 模块名称

✅ **新名称**: `yt_dlp_gui`  
❌ **旧名称**: `yt_dl_gui` (已废弃)

## 常见命令

```bash
# 运行测试
pytest

# 编译翻译
python -m yt_dlp_gui.compile_locales

# 代码格式化
black yt_dlp_gui/

# 代码检查
flake8 yt_dlp_gui/

# 清理构建
rm -rf build dist  # Linux/macOS
rmdir /s /q build dist  # Windows
```

## 文档

- **README.md** - 项目说明（英文）
- **README_zh.md** - 项目说明（中文）
- **BUILD.md** - 构建指南（英文）
- **BUILD_zh.md** - 构建指南（中文）
- **CONTRIBUTING.md** - 贡献指南
- **REFACTORING_SUMMARY.md** - 重构总结

## 支持

- **Issues**: GitHub Issues
- **文档**: 查看 BUILD.md 获取详细说明
