"""
Project Setup Verification Script
This script checks if all required components are properly set up.

Usage:
python verify_setup.py
"""

import os
import sys
import django
from pathlib import Path

def print_header(text):
    """Print a formatted header"""
    print("\n" + "="*60)
    print(f"  {text}")
    print("="*60)

def print_check(status, message):
    """Print a check result"""
    symbol = "✓" if status else "✗"
    color = "\033[92m" if status else "\033[91m"
    reset = "\033[0m"
    print(f"{color}{symbol}{reset} {message}")

def verify_environment():
    """Verify Python environment"""
    print_header("Python Environment")
    
    # Python version
    version = f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
    print_check(sys.version_info >= (3, 8), f"Python version: {version}")
    
    # Virtual environment
    in_venv = hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix)
    print_check(in_venv, "Virtual environment active")

def verify_dependencies():
    """Verify required packages"""
    print_header("Dependencies")
    
    packages = {
        'django': 'Django',
        'PIL': 'Pillow',
    }
    
    for module, name in packages.items():
        try:
            __import__(module)
            print_check(True, f"{name} is installed")
        except ImportError:
            print_check(False, f"{name} is NOT installed")
            print(f"  Install with: pip install {name}")

def verify_project_structure():
    """Verify project folder structure"""
    print_header("Project Structure")
    
    base_path = Path(__file__).parent
    
    required_dirs = [
        'digital_identity_hub',
        'core',
        'core/migrations',
        'templates',
        'templates/core',
        'static',
        'static/css',
        'static/js',
    ]
    
    for dir_name in required_dirs:
        path = base_path / dir_name
        exists = path.is_dir()
        print_check(exists, f"Directory: {dir_name}")

def verify_files():
    """Verify required files"""
    print_header("Required Files")
    
    base_path = Path(__file__).parent
    
    required_files = [
        'manage.py',
        'requirements.txt',
        'digital_identity_hub/__init__.py',
        'digital_identity_hub/settings.py',
        'digital_identity_hub/urls.py',
        'digital_identity_hub/wsgi.py',
        'core/__init__.py',
        'core/models.py',
        'core/views.py',
        'core/urls.py',
        'core/admin.py',
        'core/apps.py',
        'templates/core/index.html',
        'templates/core/project_detail.html',
        'static/css/style.css',
        'static/js/main.js',
        'README.md',
        'QUICKSTART.md',
    ]
    
    for file_name in required_files:
        path = base_path / file_name
        exists = path.is_file()
        print_check(exists, f"File: {file_name}")

def verify_django():
    """Verify Django setup"""
    print_header("Django Configuration")
    
    try:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'digital_identity_hub.settings')
        django.setup()
        print_check(True, "Django configured correctly")
        
        # Check apps
        from django.apps import apps
        installed_apps = [app.name for app in apps.get_app_configs()]
        
        required_apps = ['core']
        for app in required_apps:
            installed = f"core" in installed_apps
            print_check(installed, f"App 'core' installed")
            
    except Exception as e:
        print_check(False, f"Django configuration error: {str(e)}")

def verify_database():
    """Verify database setup"""
    print_header("Database")
    
    try:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'digital_identity_hub.settings')
        django.setup()
        
        from django.db import connection
        
        # Test database connection
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
            print_check(True, "Database connection successful")
        
        # Check tables
        from core.models import Profile, Skill, Project, TimelineEntry, Contact
        
        models = [
            ('Profile', Profile),
            ('Skill', Skill),
            ('Project', Project),
            ('TimelineEntry', TimelineEntry),
            ('Contact', Contact),
        ]
        
        for model_name, model_class in models:
            try:
                model_class.objects.count()
                print_check(True, f"Model '{model_name}' table exists")
            except Exception as e:
                print_check(False, f"Model '{model_name}' table error: {str(e)}")
                
    except Exception as e:
        print_check(False, f"Database error: {str(e)}")

def verify_static_files():
    """Verify static files"""
    print_header("Static Files")
    
    base_path = Path(__file__).parent
    
    static_files = [
        'static/css/style.css',
        'static/js/main.js',
    ]
    
    for file_name in static_files:
        path = base_path / file_name
        exists = path.is_file()
        
        if exists:
            size = path.stat().st_size
            print_check(True, f"{file_name} ({size} bytes)")
        else:
            print_check(False, file_name)

def verify_templates():
    """Verify template files"""
    print_header("Templates")
    
    base_path = Path(__file__).parent
    
    templates = [
        'templates/core/index.html',
        'templates/core/project_detail.html',
    ]
    
    for template_name in templates:
        path = base_path / template_name
        exists = path.is_file()
        
        if exists:
            size = path.stat().st_size
            print_check(True, f"{template_name} ({size} bytes)")
        else:
            print_check(False, template_name)

def main():
    """Run all verification checks"""
    
    print("\n")
    print("╔═══════════════════════════════════════════════════════╗")
    print("║  Digital Identity Hub - Setup Verification           ║")
    print("╚═══════════════════════════════════════════════════════╝")
    
    try:
        verify_environment()
        verify_dependencies()
        verify_project_structure()
        verify_files()
        verify_django()
        verify_database()
        verify_static_files()
        verify_templates()
        
        print_header("Verification Complete")
        print("\n✓ All checks completed!")
        print("\nNext steps:")
        print("1. If any checks failed, run: python manage.py migrate")
        print("2. Create a superuser: python manage.py createsuperuser")
        print("3. Start the server: python manage.py runserver")
        print("4. Visit: http://localhost:8000")
        print("\n")
        
    except Exception as e:
        print(f"\n✗ Verification error: {str(e)}")
        print("\nPlease check the error message above and try again.")

if __name__ == '__main__':
    main()
