# API Documentation

This document describes the API endpoints and how to interact with the Digital Identity Hub programmatically.

## 📍 Base URLs

- **Development**: `http://localhost:8000`
- **Production**: `https://yourdomain.com`

## 🔐 Authentication

Currently, the public-facing endpoints don't require authentication. However, Django admin and data modification requires authentication.

Admin access:
- **URL**: `/admin/`
- **Method**: GET
- **Credentials**: Superuser credentials

## 📡 Public Endpoints

### 1. Homepage

**Endpoint**: `/`

**Method**: `GET`

**Description**: Returns the homepage with all portfolio sections

**Response**: HTML page with embedded context data

**Status Codes**:
- `200`: Success
- `500`: Server error

**Example**:
```bash
curl http://localhost:8000/
```

### 2. Project Detail

**Endpoint**: `/project/<slug>/`

**Method**: `GET`

**Description**: Returns detail page for a specific project

**URL Parameters**:
- `slug` (string, required): Project URL slug (e.g., "ecommerce-platform")

**Response**: HTML page with project details

**Status Codes**:
- `200`: Success
- `404`: Project not found

**Example**:
```bash
curl http://localhost:8000/project/ecommerce-platform/
```

### 3. Contact Form Submission

**Endpoint**: `/api/contact/`

**Method**: `POST`

**Description**: Submit a contact form message

**Content-Type**: `application/json`

**Request Body**:
```json
{
    "name": "John Doe",
    "email": "john@example.com",
    "subject": "Portfolio Inquiry",
    "message": "I'm interested in your work..."
}
```

**Response**:
```json
{
    "success": true,
    "message": "Thank you! Your message has been received."
}
```

**Status Codes**:
- `200`: Successfully submitted
- `400`: Bad request / validation error
- `405`: Method not allowed

**Example**:
```bash
curl -X POST http://localhost:8000/api/contact/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Jane Doe",
    "email": "jane@example.com",
    "subject": "Hello",
    "message": "I love your portfolio!"
  }'
```

**JavaScript Example**:
```javascript
fetch('/api/contact/', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': getCookie('csrftoken')
    },
    body: JSON.stringify({
        name: 'John Doe',
        email: 'john@example.com',
        subject: 'Inquiry',
        message: 'Hello!'
    })
})
.then(response => response.json())
.then(data => console.log(data))
.catch(error => console.error('Error:', error));
```

## 🔧 Django ORM API (Python)

Access models programmatically via Django shell:

```bash
python manage.py shell
```

### Profile Model

```python
from core.models import Profile

# Get all profiles
profiles = Profile.objects.all()

# Get first profile
profile = Profile.objects.first()

# Access profile data
print(profile.name)
print(profile.email)
print(profile.bio)
print(profile.github_url)

# Update profile
profile.name = "New Name"
profile.save()

# Create new profile
new_profile = Profile.objects.create(
    name="John Doe",
    title="Developer",
    email="john@example.com",
    location="San Francisco"
)
```

### Skill Model

```python
from core.models import Skill

# Get all skills
skills = Skill.objects.all()

# Filter by category
frontend_skills = Skill.objects.filter(category='frontend')

# Filter by proficiency
expert_skills = Skill.objects.filter(proficiency='expert')

# Order by order field
ordered_skills = Skill.objects.order_by('order')

# Count skills
total_skills = Skill.objects.count()

# Create skill
new_skill = Skill.objects.create(
    name="Python",
    category="backend",
    proficiency="expert",
    icon="🐍",
    order=1
)

# Update skill
skill = Skill.objects.get(name="Python")
skill.proficiency = "advanced"
skill.save()

# Delete skill
skill.delete()
```

### Project Model

```python
from core.models import Project
from datetime import date

# Get all projects
projects = Project.objects.all()

# Get featured projects
featured = Project.objects.filter(featured=True)

# Get recent projects
recent = Project.objects.order_by('-start_date')[:5]

# Search projects
search_results = Project.objects.filter(title__icontains="ecommerce")

# Create project
project = Project.objects.create(
    title="My Project",
    slug="my-project",
    description="Project description",
    technologies="Django, React",
    start_date=date(2024, 1, 1),
    featured=True
)

# Get project by slug
project = Project.objects.get(slug="my-project")

# Update project
project.description = "Updated description"
project.end_date = date(2024, 6, 30)
project.save()
```

### TimelineEntry Model

```python
from core.models import TimelineEntry
from datetime import date

# Get all timeline entries
timeline = TimelineEntry.objects.all()

# Filter by type
education = TimelineEntry.objects.filter(entry_type='education')
experience = TimelineEntry.objects.filter(entry_type='experience')

# Order by start date
ordered = TimelineEntry.objects.order_by('-start_date')

# Create timeline entry
entry = TimelineEntry.objects.create(
    title="Software Engineer",
    entry_type="experience",
    organization="Tech Company",
    description="Developed web applications",
    start_date=date(2023, 1, 1),
    icon="💼"
)

# Get entries for specific year
year_2024 = TimelineEntry.objects.filter(
    start_date__year=2024
)
```

### Contact Model

```python
from core.models import Contact

# Get all contact messages
messages = Contact.objects.all()

# Get unread messages
unread = Contact.objects.filter(read=False)

# Get messages by email
user_messages = Contact.objects.filter(email="user@example.com")

# Mark as read
message = Contact.objects.first()
message.read = True
message.save()

# Get recent messages (last 10)
recent = Contact.objects.order_by('-created_at')[:10]

# Delete old messages
from datetime import datetime, timedelta
old_date = datetime.now() - timedelta(days=30)
Contact.objects.filter(created_at__lt=old_date).delete()

# Count unread
unread_count = Contact.objects.filter(read=False).count()
```

## 📊 QuerySet Methods Reference

```python
# Filtering
Model.objects.filter(field=value)
Model.objects.exclude(field=value)
Model.objects.get(id=1)

# Ordering
Model.objects.order_by('field')
Model.objects.order_by('-field')  # Descending

# Slicing
Model.objects.all()[:10]  # First 10
Model.objects.all()[10:20]  # 10-20

# Aggregation
from django.db.models import Count, Sum, Avg
Model.objects.aggregate(total=Count('id'))

# Exists
Model.objects.filter(field=value).exists()

# Count
Model.objects.filter(field=value).count()

# Delete
Model.objects.filter(field=value).delete()

# Update
Model.objects.filter(field=value).update(other_field=new_value)

# Values
Model.objects.values('field1', 'field2')

# Distinct
Model.objects.values('field').distinct()

# Exists
if Model.objects.filter(id=1).exists():
    print("Found")
```

## 🔗 URL Routing Reference

```python
# Reverse URL lookup
from django.urls import reverse

# Get URL by name
home_url = reverse('core:index')  # Returns '/'
project_url = reverse('core:project_detail', args=['project-slug'])  # Returns '/project/project-slug/'
```

## 📈 Examples

### Get Profile Statistics

```python
from core.models import Profile, Skill, Project, TimelineEntry

# Count total items
profile_count = Profile.objects.count()
skill_count = Skill.objects.count()
project_count = Project.objects.count()
timeline_count = TimelineEntry.objects.count()

print(f"Portfolio Statistics:")
print(f"Profile: {profile_count}")
print(f"Skills: {skill_count}")
print(f"Projects: {project_count}")
print(f"Timeline: {timeline_count}")
```

### Get Skills by Category

```python
from core.models import Skill

skills_by_category = {}
for skill in Skill.objects.all():
    if skill.category not in skills_by_category:
        skills_by_category[skill.category] = []
    skills_by_category[skill.category].append(skill)

for category, skills in skills_by_category.items():
    print(f"{category.upper()}: {', '.join([s.name for s in skills])}")
```

### Export Data to JSON

```python
import json
from core.models import Project
from django.core.serializers import serialize

# Serialize projects
projects_json = serialize('json', Project.objects.all())
print(projects_json)

# Save to file
with open('projects.json', 'w') as f:
    f.write(projects_json)
```

### Import Data from JSON

```python
from django.core.management import call_command

call_command('loaddata', 'projects.json')
```

## 🔒 Admin API

The Django admin provides a REST-like interface at `/admin/`

### Admin URLs

- `/admin/auth/user/` - User management
- `/admin/core/profile/` - Profile management
- `/admin/core/skill/` - Skill management
- `/admin/core/project/` - Project management
- `/admin/core/timelineentry/` - Timeline management
- `/admin/core/contact/` - Contact messages

### Admin Actions (Example)

```python
# In admin.py
from django.contrib import admin

@admin.action(description="Mark selected messages as read")
def mark_as_read(modeladmin, request, queryset):
    queryset.update(read=True)

class ContactAdmin(admin.ModelAdmin):
    actions = [mark_as_read]
```

## 🚀 Creating REST API (Optional Enhancement)

To add a full REST API, install Django REST Framework:

```bash
pip install djangorestframework
```

Then create serializers and viewsets:

```python
# In core/serializers.py
from rest_framework import serializers
from core.models import Profile, Skill, Project

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['id', 'name', 'category', 'proficiency']

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'title', 'slug', 'description', 'technologies', 'featured']

class ProfileSerializer(serializers.ModelSerializer):
    skills = SkillSerializer(many=True, read_only=True)
    class Meta:
        model = Profile
        fields = ['name', 'title', 'email', 'bio', 'skills']
```

## 📞 Support

For API issues:
1. Check Django documentation: https://docs.djangoproject.com/
2. Check Django REST Framework: https://www.django-rest-framework.org/
3. Review code comments
4. Check troubleshooting guide

---

**API Version**: 1.0  
**Last Updated**: 2024  
**Status**: Stable
