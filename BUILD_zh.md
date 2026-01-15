# PyInstaller 打包说明

本指南说明如何使用 PyInstaller 构建 yt-dlp-gui 的独立可执行文件。

## 前置要求

1. **安装 PyInstaller**
   ```bash
   pip install pyinstaller
   ```

2. **安装所有依赖**
   ```bash
   pip install -r requirements.txt
   pip install -r requirements-dev.txt
   ```

## 构建

### Windows

运行构建脚本：
```cmd
build.cmd
```

或手动构建：
```cmd
pyinstaller --clean yt-dlp-gui.spec
```

### Linux/macOS

运行构建脚本：
```bash
chmod +x build.sh
./build.sh
```

或手动构建：
```bash
pyinstaller --clean yt-dlp-gui.spec
```

## 输出

可执行文件将在以下位置创建：
```
dist/yt-dlp-gui/
```

### Windows
- `dist/yt-dlp-gui/yt-dlp-gui.exe`

### Linux/macOS
- `dist/yt-dlp-gui/yt-dlp-gui`

## 分发

要分发应用程序：

1. **压缩整个文件夹**
   ```bash
   # Windows
   Compress-Archive -Path dist\yt-dlp-gui -DestinationPath yt-dlp-gui-windows.zip
   
   # Linux/macOS
   cd dist
   tar -czf yt-dlp-gui-linux.tar.gz yt-dlp-gui/
   ```

2. **分享压缩文件**给用户

用户可以解压并运行可执行文件，无需安装 Python 或任何依赖项。

## 自定义

### 添加图标

1. 创建或获取 `.ico` 文件（Windows）或 `.icns` 文件（macOS）
2. 编辑 `yt-dlp-gui.spec`：
   ```python
   exe = EXE(
       ...
       icon='path/to/icon.ico',  # 添加这一行
       ...
   )
   ```

### 单文件构建

要创建单个可执行文件而不是文件夹，请参阅 [BUILD.md](BUILD.md) 获取详细说明。

## 故障排除

### 缺少模块

如果运行可执行文件时出现导入错误：

1. 将缺少的模块添加到 `yt-dlp-gui.spec` 的 `hiddenimports` 中
2. 重新构建

### 缺少数据文件

如果语言文件或其他数据丢失：

1. 检查 `yt-dlp-gui.spec` 中的 `datas` 部分
2. 添加缺少的文件
3. 重新构建

详细信息请参阅 [BUILD.md](BUILD.md)。

## 注意事项

- 可执行文件是平台特定的（Windows .exe 无法在 Linux 上运行）
- 在每个目标平台上构建以获得最佳兼容性
- FFmpeg 不包含在内 - 用户需要单独安装
- 可执行文件大小对于 PyInstaller 应用程序来说是正常的（100-200 MB）

## 支持

如果遇到问题：
1. 查看 PyInstaller 文档：https://pyinstaller.org/
2. 在 GitHub 上提交 issue 并附上构建日志
3. 包含您的操作系统和 Python 版本
