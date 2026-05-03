"""
Database models for the digital_identity_hub project.
Models define the structure of data stored in the database.

Models included:
- Profile: Personal profile information
- Skill: Technical and soft skills
- Project: Portfolio projects
- TimelineEntry: Career/education timeline events
- Contact: Contact form submissions

Each model is automatically registered in Django admin.
"""

from django.db import models
from django.utils import timezone


class Profile(models.Model):
    """
    Represents the user's main profile information.
    This is typically a singleton (only one profile per portfolio site).
    """
    name = models.CharField(max_length=200, help_text="Your full name")
    title = models.CharField(max_length=200, help_text="Your professional title/role")
    bio = models.TextField(help_text="Brief bio about yourself")
    profile_image = models.ImageField(upload_to='profile/', null=True, blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, help_text="Optional phone number")
    location = models.CharField(max_length=100, help_text="Your location")
    
    # Social links
    github_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    
    # Metadata
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = "Profile"
    
    def __str__(self):
        return self.name


class Skill(models.Model):
    """
    Represents a technical or soft skill.
    Skills are displayed on the portfolio with proficiency levels.
    """
    PROFICIENCY_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
        ('expert', 'Expert'),
    ]
    
    CATEGORY_CHOICES = [
        ('frontend', 'Frontend'),
        ('backend', 'Backend'),
        ('database', 'Database'),
        ('tools', 'Tools & Platforms'),
        ('soft', 'Soft Skills'),
        ('other', 'Other'),
    ]
    
    name = models.CharField(max_length=100, help_text="Skill name (e.g., Python, React)")
    category = models.CharField(
        max_length=20, 
        choices=CATEGORY_CHOICES,
        help_text="Category for organizing skills"
    )
    proficiency = models.CharField(
        max_length=20, 
        choices=PROFICIENCY_CHOICES,
        help_text="Your proficiency level"
    )
    icon = models.CharField(
        max_length=100, 
        blank=True,
        help_text="CSS class or emoji for icon (e.g., 'fab fa-python' or '🐍')"
    )
    order = models.PositiveIntegerField(
        default=0,
        help_text="Display order (lower numbers appear first)"
    )
    
    # Metadata
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['order', 'name']
        verbose_name_plural = "Skills"
    
    def __str__(self):
        return f"{self.name} ({self.get_proficiency_display()})"


class Project(models.Model):
    """
    Represents a portfolio project.
    Projects showcase your work with descriptions, technologies, and links.
    """
    title = models.CharField(max_length=200, help_text="Project name")
    slug = models.SlugField(unique=True, help_text="URL-friendly name (auto-generated)")
    description = models.TextField(help_text="Project description")
    long_description = models.TextField(blank=True, help_text="Detailed project description")
    
    # Links and media
    image = models.ImageField(upload_to='projects/', help_text="Project preview image")
    demo_url = models.URLField(blank=True, help_text="Link to live demo")
    github_url = models.URLField(blank=True, help_text="Link to GitHub repository")
    
    # Technologies used (comma-separated or you can create a separate Tech model)
    technologies = models.CharField(
        max_length=500, 
        help_text="Technologies used (e.g., Django, React, PostgreSQL)"
    )
    
    # Project details
    start_date = models.DateField(help_text="Project start date")
    end_date = models.DateField(null=True, blank=True, help_text="Project end date (leave blank if ongoing)")
    
    # Display settings
    featured = models.BooleanField(default=False, help_text="Show on homepage")
    order = models.PositiveIntegerField(
        default=0,
        help_text="Display order (lower numbers appear first)"
    )
    
    # Metadata
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-start_date', 'order']
        verbose_name_plural = "Projects"
    
    def __str__(self):
        return self.title


class TimelineEntry(models.Model):
    """
    Represents a timeline entry (education, work experience, achievement).
    Used to create an interactive timeline on the portfolio.
    """
    ENTRY_TYPE_CHOICES = [
        ('education', 'Education'),
        ('experience', 'Work Experience'),
        ('achievement', 'Achievement'),
        ('event', 'Event'),
    ]
    
    title = models.CharField(max_length=200, help_text="Entry title")
    entry_type = models.CharField(
        max_length=20,
        choices=ENTRY_TYPE_CHOICES,
        help_text="Type of timeline entry"
    )
    organization = models.CharField(
        max_length=200,
        help_text="Organization/Company/School name"
    )
    description = models.TextField(help_text="Details about this entry")
    
    # Timeline positioning
    start_date = models.DateField(help_text="Start date")
    end_date = models.DateField(null=True, blank=True, help_text="End date (leave blank if ongoing)")
    
    # Display settings
    icon = models.CharField(
        max_length=100,
        blank=True,
        help_text="Icon class or emoji for this entry"
    )
    order = models.PositiveIntegerField(
        default=0,
        help_text="Display order (lower numbers appear first)"
    )
    
    # Metadata
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-start_date', 'order']
        verbose_name_plural = "Timeline Entries"
    
    def __str__(self):
        return f"{self.title} - {self.organization}"


class Contact(models.Model):
    """
    Stores contact form submissions from website visitors.
    These can be reviewed and managed through the Django admin.
    """
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    
    # Metadata
    created_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False, help_text="Whether this message has been read")
    
    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = "Contact Messages"
    
    def __str__(self):
        return f"{self.name} - {self.subject}"
