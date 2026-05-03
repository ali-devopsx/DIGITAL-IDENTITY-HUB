#!/bin/bash

# ==========================================================================
# Digital Identity Hub - Setup Script for macOS/Linux
# ==========================================================================
# This script automates the setup process for the project
#
# Usage: bash setup.sh or ./setup.sh
# ==========================================================================

echo ""
echo "========================================================="
echo "  Digital Identity Hub - Automated Setup (macOS/Linux)"
echo "========================================================="
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null
then
    echo "Error: Python 3 is not installed"
    echo "Please install Python 3.8 or higher"
    exit 1
fi

echo "[1/5] Creating virtual environment..."
python3 -m venv venv
if [ $? -ne 0 ]; then
    echo "Error: Failed to create virtual environment"
    exit 1
fi
echo "Successfully created virtual environment"

echo ""
echo "[2/5] Activating virtual environment..."
source venv/bin/activate
echo "Successfully activated virtual environment"

echo ""
echo "[3/5] Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt
if [ $? -ne 0 ]; then
    echo "Error: Failed to install dependencies"
    exit 1
fi
echo "Successfully installed dependencies"

echo ""
echo "[4/5] Setting up database..."
python manage.py migrate
if [ $? -ne 0 ]; then
    echo "Error: Failed to create database"
    exit 1
fi
echo "Successfully created database"

echo ""
echo "[5/5] Populating sample data..."
python manage.py shell < populate_sample_data.py
if [ $? -ne 0 ]; then
    echo "Warning: Could not populate sample data automatically"
    echo "You can run: python manage.py shell"
    echo "Then: exec(open('populate_sample_data.py').read())"
fi

echo ""
echo "========================================================="
echo "  Setup Complete!"
echo "========================================================="
echo ""
echo "To create a superuser (admin account), run:"
echo "  python manage.py createsuperuser"
echo ""
echo "To start the development server, run:"
echo "  python manage.py runserver"
echo ""
echo "Then visit:"
echo "  Homepage: http://localhost:8000"
echo "  Admin: http://localhost:8000/admin"
echo ""
