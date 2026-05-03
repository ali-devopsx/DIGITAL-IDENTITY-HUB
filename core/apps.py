"""
App configuration for the 'core' app.
This file configures the core app and is automatically imported by Django.
It allows customization of the app's behavior.
"""

from django.apps import AppConfig


class CoreConfig(AppConfig):
    """Configuration class for the core app."""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'
    verbose_name = 'Digital Identity Hub'
