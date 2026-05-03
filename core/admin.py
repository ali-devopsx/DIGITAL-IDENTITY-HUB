"""
Django admin configuration for the core app.
Registers all models and customizes their admin interface.
Access at: http://localhost:8000/admin/

Features:
- Custom admin classes for better UX
- List displays and filtering
- Search functionality
- Inline editing where applicable
"""

from django.contrib import admin
from .models import Profile, Skill, Project, TimelineEntry, Contact


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """
    Admin interface for Profile model.
    Profile represents the site owner's personal information.
    """
    list_display = ('name', 'title', 'email', 'location', 'updated_at')
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'title', 'bio', 'profile_image')
        }),
        ('Contact Information', {
            'fields': ('email', 'phone', 'location')
        }),
        ('Social Links', {
            'fields': ('github_url', 'linkedin_url', 'twitter_url', 'instagram_url'),
            'classes': ('collapse',)  # Collapsible section
        }),
        ('Metadata', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    readonly_fields = ('created_at', 'updated_at')


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    """
    Admin interface for Skill model.
    Allows managing technical and soft skills.
    """
    list_display = ('name', 'category', 'proficiency', 'order')
    list_filter = ('category', 'proficiency')  # Filter by category and proficiency
    search_fields = ('name',)  # Search by skill name
    ordering = ('order', 'name')
    
    fieldsets = (
        ('Skill Information', {
            'fields': ('name', 'category', 'proficiency', 'icon')
        }),
        ('Display Settings', {
            'fields': ('order',)
        }),
        ('Metadata', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    readonly_fields = ('created_at', 'updated_at')


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    """
    Admin interface for Project model.
    Manage portfolio projects with full details.
    """
    list_display = ('title', 'start_date', 'featured', 'order')
    list_filter = ('featured', 'start_date')  # Filter projects
    search_fields = ('title', 'description')  # Full-text search
    readonly_fields = ('created_at', 'updated_at', 'slug')
    ordering = ('-start_date', 'order')
    
    # Auto-generate slug from title if not provided
    prepopulated_fields = {'slug': ('title',)}
    
    fieldsets = (
        ('Project Information', {
            'fields': ('title', 'slug', 'description', 'long_description')
        }),
        ('Project Details', {
            'fields': ('technologies', 'start_date', 'end_date')
        }),
        ('Media & Links', {
            'fields': ('image', 'demo_url', 'github_url')
        }),
        ('Display Settings', {
            'fields': ('featured', 'order')
        }),
        ('Metadata', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(TimelineEntry)
class TimelineEntryAdmin(admin.ModelAdmin):
    """
    Admin interface for TimelineEntry model.
    Create career and education timeline.
    """
    list_display = ('title', 'entry_type', 'organization', 'start_date')
    list_filter = ('entry_type', 'start_date')  # Filter by type and date
    search_fields = ('title', 'organization', 'description')  # Search
    ordering = ('-start_date', 'order')
    
    fieldsets = (
        ('Timeline Information', {
            'fields': ('title', 'entry_type', 'organization', 'description')
        }),
        ('Timeline Period', {
            'fields': ('start_date', 'end_date')
        }),
        ('Display Settings', {
            'fields': ('icon', 'order')
        }),
        ('Metadata', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    readonly_fields = ('created_at', 'updated_at')


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """
    Admin interface for Contact model.
    Review and manage contact form submissions.
    """
    list_display = ('name', 'email', 'subject', 'created_at', 'read')
    list_filter = ('read', 'created_at')  # Filter by read status and date
    search_fields = ('name', 'email', 'subject', 'message')  # Full search
    readonly_fields = ('created_at', 'name', 'email', 'subject', 'message')
    ordering = ('-created_at',)
    
    fieldsets = (
        ('Message Information', {
            'fields': ('name', 'email', 'subject')
        }),
        ('Message Content', {
            'fields': ('message',)
        }),
        ('Status', {
            'fields': ('read', 'created_at')
        }),
    )
    
    # Prevent editing - only allow viewing and marking as read
    def has_add_permission(self, request):
        """Prevent adding messages via admin - only from website form."""
        return False
    
    def has_delete_permission(self, request, obj=None):
        """Allow deleting messages."""
        return True
