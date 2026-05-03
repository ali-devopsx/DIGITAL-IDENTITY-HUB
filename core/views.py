"""
Views for the core app.
Views are functions/classes that handle HTTP requests and return responses.
Each view retrieves data from the database and renders it with templates.

Views included:
- index: Homepage displaying all sections
- project_detail: Detailed view of a single project
- send_contact: Handle contact form submissions
"""

from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.conf import settings
import json
from .models import Profile, Skill, Project, TimelineEntry, Contact


def index(request):
    """
    Homepage view - displays all portfolio sections.
    Retrieves all data from models and passes to template.
    
    Template: core/index.html
    Context:
    - profile: User's profile information
    - skills: All skills grouped by category
    - projects: Featured projects
    - timeline: Career/education timeline
    """
    # Retrieve profile data (typically only one exists)
    profile = Profile.objects.first()
    
    # Retrieve and organize skills by category
    skills = Skill.objects.all().order_by('order')
    skills_by_category = {}
    for skill in skills:
        if skill.category not in skills_by_category:
            skills_by_category[skill.category] = []
        skills_by_category[skill.category].append(skill)
    
    # Retrieve featured projects
    projects = Project.objects.filter(featured=True).order_by('order')[:6]
    
    # Retrieve timeline entries
    timeline = TimelineEntry.objects.all().order_by('-start_date')
    
    # Prepare context dictionary with all data
    context = {
        'profile': profile,
        'skills_by_category': skills_by_category,
        'projects': projects,
        'timeline': timeline,
    }
    
    return render(request, 'core/index.html', context)


def project_detail(request, slug):
    """
    Detailed project view - displays complete project information.
    
    Args:
        slug: URL-friendly project identifier
    
    Template: core/project_detail.html
    Context:
    - project: The detailed project object
    - all_projects: All projects for navigation
    """
    # Get the specific project or return 404 error
    project = get_object_or_404(Project, slug=slug)
    
    # Get all projects for project navigation
    all_projects = Project.objects.all().order_by('-start_date')
    
    context = {
        'project': project,
        'all_projects': all_projects,
    }
    
    return render(request, 'core/project_detail.html', context)


@require_http_methods(["POST"])
@csrf_exempt  # CSRF protection handled by CSRF token in form
def send_contact(request):
    """
    Handle contact form submissions via AJAX.
    Receives form data and saves to Contact model.
    
    Request body (JSON):
    {
        "name": "John Doe",
        "email": "john@example.com",
        "subject": "Inquiry",
        "message": "Your message here"
    }
    
    Response (JSON):
    {
        "success": true/false,
        "message": "Response message"
    }
    """
    try:
        # Parse JSON data from request
        data = json.loads(request.body)
        
        # Create new Contact instance with form data
        contact = Contact.objects.create(
            name=data.get('name', '').strip(),
            email=data.get('email', '').strip(),
            subject=data.get('subject', '').strip(),
            message=data.get('message', '').strip(),
        )
        
        # Optional: Send email notification to site owner
        # Uncomment if you have email configured
        # send_mail(
        #     f"New Contact: {contact.subject}",
        #     f"From: {contact.name} ({contact.email})\n\n{contact.message}",
        #     settings.DEFAULT_FROM_EMAIL,
        #     [settings.DEFAULT_FROM_EMAIL],
        #     fail_silently=True,
        # )
        
        return JsonResponse({
            'success': True,
            'message': 'Thank you! Your message has been received.'
        })
    
    except Exception as e:
        # Return error response if something goes wrong
        return JsonResponse({
            'success': False,
            'message': 'An error occurred. Please try again.'
        }, status=400)
