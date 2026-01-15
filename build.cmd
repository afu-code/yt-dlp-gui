@echo off
REM Build script for Windows using PyInstaller

echo Building yt-dlp-gui for Windows...
echo.

REM Clean previous builds
if exist "build" rmdir /s /q build
if exist "dist" rmdir /s /q dist

REM Run PyInstaller
pyinstaller --clean yt-dlp-gui.spec

if %ERRORLEVEL% EQU 0 (
    echo.
    echo Build successful!
    echo Executable is in: dist\yt-dlp-gui\
    echo.
) else (
    echo.
    echo Build failed!
    echo.
    exit /b 1
)
