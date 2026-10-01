@echo off
cd /d "%~dp0"
if exist "DJANGO_TRAINING\manage.py" (
    cd DJANGO_TRAINING
)

if exist "venv\Scripts\activate.bat" (
    call venv\Scripts\activate.bat
)

echo Starting Django development server at http://127.0.0.1:8000/ ...
python manage.py runserver
pause
