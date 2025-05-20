@echo off
title Cyber Hygiene Toolkit - LUNIX WEB
cls
echo.
echo  ============================================
echo     CYBER HYGIENE TOOLKIT FOR WINDOWS USERS
echo  ============================================
echo.
echo       Developed by: LUNIX WEB
echo     Your Vision, Our Code
echo --------------------------------------------
echo.
echo [1] Enable Firewall
echo [2] Run Windows Defender Quick Scan
echo [3] Clear Junk Files
echo [4] Check Disk Space
echo [5] Show System Info
echo [6] Exit
echo.

set /p choice=Enter your choice: 
if "%choice%"=="1" powershell -ExecutionPolicy Bypass -File scripts\enable_firewall.ps1
if "%choice%"=="2" powershell -ExecutionPolicy Bypass -File scripts\defender_quickscan.ps1
if "%choice%"=="3" powershell -ExecutionPolicy Bypass -File scripts\clear_junk.ps1
if "%choice%"=="4" powershell -ExecutionPolicy Bypass -File scripts\check_disk.ps1
if "%choice%"=="5" powershell -ExecutionPolicy Bypass -File scripts\system_info.ps1
if "%choice%"=="6" exit
pause
