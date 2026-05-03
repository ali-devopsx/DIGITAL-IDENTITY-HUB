#!/usr/bin/env python
"""
Django's command-line utility for administrative tasks.
This file is used to run management commands like:
- python manage.py runserver (start development server)
- python manage.py makemigrations (create database migrations)
- python manage.py migrate (apply migrations)
- python manage.py createsuperuser (create admin user)
- python manage.py collectstatic (collect static files for production)
"""

import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'digital_identity_hub.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
