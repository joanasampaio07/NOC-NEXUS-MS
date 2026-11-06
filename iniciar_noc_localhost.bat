@echo off
title NOC & SOC NEXUS-M&S - Web Server
set PORT=80
if not "%~1"=="" set PORT=%~1

echo ========================================================
echo   NEXUS-M&S - NOC / SOC WAR ROOM
echo   Iniciando Servidor Web Local na porta %PORT%...
echo   Localhost:  http://localhost
echo   Rede Local: http://192.168.15.11
echo ========================================================
cd /d "%~dp0"

:: Aguarda 1 segundo para garantir que o Python subiu antes do navegador carregar
if "%PORT%"=="80" (
    start "" cmd /c "timeout /t 1 /nobreak >nul & start http://localhost"
) else (
    start "" cmd /c "timeout /t 1 /nobreak >nul & start http://localhost:%PORT%"
)

python -m http.server %PORT% --bind 0.0.0.0
pause
