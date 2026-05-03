"""
WSGI config for digital_identity_hub project.
WSGI (Web Server Gateway Interface) is the standard interface for Python web applications.
This is the entry point for production-ready servers like Gunicorn or uWSGI.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'digital_identity_hub.settings')

application = get_wsgi_application()
