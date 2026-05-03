"""
Project-level URL router for digital_identity_hub.
This file defines the main URL patterns for the entire project.
It routes requests to different apps and includes URL patterns from the 'core' app.

URL patterns:
- /admin/ - Django admin panel
- / - Homepage and all core app URLs (from core.urls)
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Admin interface - access at http://localhost:8000/admin/
    path('admin/', admin.site.urls),
    
    # Include URLs from the core app - all portfolio URLs
    path('', include('core.urls')),
]

# Serve media files during development
# In production, a web server (nginx, Apache) serves these files
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
