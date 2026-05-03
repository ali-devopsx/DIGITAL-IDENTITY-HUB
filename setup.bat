@echo off
REM ==========================================================================
REM Digital Identity Hub - Setup Script for Windows
REM ==========================================================================
REM This script automates the setup process for the project
REM
REM Usage: Run this file from the project root directory
REM ==========================================================================

echo.
echo =========================================================
echo   Digital Identity Hub - Automated Setup (Windows)
echo =========================================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed or not in PATH
    echo Please install Python 3.8 or higher from https://www.python.org
    exit /b 1
)

echo [1/5] Creating virtual environment...
python -m venv venv
if errorlevel 1 (
    echo Error: Failed to create virtual environment
    exit /b 1
)
echo Successfully created virtual environment

echo.
echo [2/5] Activating virtual environment...
call venv\Scripts\activate.bat
echo Successfully activated virtual environment

echo.
echo [3/5] Installing dependencies...
pip install -r requirements.txt
if errorlevel 1 (
    echo Error: Failed to install dependencies
    exit /b 1
)
echo Successfully installed dependencies

echo.
echo [4/5] Setting up database...
python manage.py migrate
if errorlevel 1 (
    echo Error: Failed to create database
    exit /b 1
)
echo Successfully created database

echo.
echo [5/5] Populating sample data...
python manage.py shell < populate_sample_data.py
if errorlevel 1 (
    echo Warning: Could not populate sample data automatically
    echo You can run: python manage.py shell and then: exec(open('populate_sample_data.py').read())
)

echo.
echo =========================================================
echo   Setup Complete!
echo =========================================================
echo.
echo To create a superuser (admin account), run:
echo   python manage.py createsuperuser
echo.
echo To start the development server, run:
echo   python manage.py runserver
echo.
echo Then visit:
echo   Homepage: http://localhost:8000
echo   Admin: http://localhost:8000/admin
echo.
pause
