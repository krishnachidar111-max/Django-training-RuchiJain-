@echo off
cd /d "%~dp0"

if exist "..\DJANGO_TRAINING\venv\Scripts\activate.bat" (
    call ..\DJANGO_TRAINING\venv\Scripts\activate.bat
)

echo Starting Task1 Django server on http://127.0.0.1:8001/ ...
python manage.py runserver 8001
pause
