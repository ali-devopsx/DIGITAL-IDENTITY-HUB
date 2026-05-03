"""
URL routing for the core app.
Maps URL patterns to view functions.

URL patterns:
- / (index): Homepage
- /project/<slug>/: Individual project detail page
- /api/contact/: Contact form submission API
"""

from django.urls import path
from . import views

# App namespace for URL reversing
app_name = 'core'

urlpatterns = [
    # Homepage - displays all portfolio sections
    path('', views.index, name='index'),
    
    # Project detail page - view individual project
    path('project/<slug:slug>/', views.project_detail, name='project_detail'),
    
    # AJAX endpoint for contact form submission
    path('api/contact/', views.send_contact, name='send_contact'),
]
