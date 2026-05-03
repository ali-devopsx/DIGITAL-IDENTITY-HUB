"""
ASGI config for digital_identity_hub project.
ASGI (Asynchronous Server Gateway Interface) is used for async applications.
This is the entry point for async-capable servers like Daphne or Uvicorn.
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'digital_identity_hub.settings')

application = get_asgi_application()
