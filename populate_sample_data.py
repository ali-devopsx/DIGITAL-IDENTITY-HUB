"""
Sample Data Population Script
This script populates the database with sample data for demonstration.

Usage:
python manage.py shell < populate_sample_data.py

Or in Django shell:
python manage.py shell
>>> exec(open('populate_sample_data.py').read())
"""

from core.models import Profile, Skill, Project, TimelineEntry
from datetime import datetime, date

# Clear existing data (optional - comment out to keep existing data)
# Profile.objects.all().delete()
# Skill.objects.all().delete()
# Project.objects.all().delete()
# TimelineEntry.objects.all().delete()

# ============================================================================
# Create Profile
# ============================================================================

profile, created = Profile.objects.get_or_create(
    id=1,  # Ensure only one profile
    defaults={
        'name': 'John Doe',
        'title': 'Full Stack Developer & Designer',
        'bio': 'Passionate about building beautiful and functional web applications. With over 5 years of experience in full-stack development, I love turning ideas into reality using modern technologies.',
        'email': 'john@example.com',
        'phone': '+1 (555) 123-4567',
        'location': 'San Francisco, CA',
        'github_url': 'https://github.com',
        'linkedin_url': 'https://linkedin.com',
        'twitter_url': 'https://twitter.com',
        'instagram_url': 'https://instagram.com',
    }
)

if created:
    print('✓ Profile created successfully')
else:
    print('✓ Profile already exists')

# ============================================================================
# Create Skills
# ============================================================================

frontend_skills = [
    ('HTML5', 'advanced', '🌐'),
    ('CSS3', 'advanced', '🎨'),
    ('JavaScript', 'advanced', '⚡'),
    ('React', 'advanced', '⚛️'),
    ('Vue.js', 'intermediate', '💚'),
    ('Responsive Design', 'expert', '📱'),
]

backend_skills = [
    ('Python', 'expert', '🐍'),
    ('Django', 'expert', '🚀'),
    ('Django REST', 'advanced', '🔌'),
    ('Node.js', 'intermediate', '🟩'),
    ('Express.js', 'intermediate', '⚙️'),
    ('FastAPI', 'intermediate', '⚡'),
]

database_skills = [
    ('PostgreSQL', 'advanced', '🐘'),
    ('MongoDB', 'intermediate', '🍃'),
    ('SQLite', 'advanced', '📄'),
    ('Redis', 'intermediate', '🔴'),
]

tools_skills = [
    ('Git & GitHub', 'advanced', '🐙'),
    ('Docker', 'intermediate', '🐳'),
    ('Linux', 'advanced', '🐧'),
    ('VS Code', 'expert', '💻'),
    ('AWS', 'intermediate', '☁️'),
]

soft_skills = [
    ('Team Collaboration', 'expert', '👥'),
    ('Communication', 'expert', '💬'),
    ('Problem Solving', 'expert', '🧩'),
    ('Project Management', 'advanced', '📊'),
]

skill_categories = [
    (frontend_skills, 'frontend'),
    (backend_skills, 'backend'),
    (database_skills, 'database'),
    (tools_skills, 'tools'),
    (soft_skills, 'soft'),
]

skills_created = 0
for skills_list, category in skill_categories:
    for order, (name, proficiency, icon) in enumerate(skills_list):
        skill, created = Skill.objects.get_or_create(
            name=name,
            defaults={
                'category': category,
                'proficiency': proficiency,
                'icon': icon,
                'order': order,
            }
        )
        if created:
            skills_created += 1

print(f'✓ {skills_created} skills created successfully')

# ============================================================================
# Create Projects
# ============================================================================

projects_data = [
    {
        'title': 'E-Commerce Platform',
        'slug': 'ecommerce-platform',
        'description': 'A full-featured e-commerce platform built with Django and React.',
        'long_description': 'Developed a comprehensive e-commerce platform with user authentication, product catalog, shopping cart, payment integration, and admin dashboard. Features include real-time inventory management, order tracking, and customer reviews.',
        'technologies': 'Django, React, PostgreSQL, Stripe API, Docker',
        'start_date': date(2023, 1, 15),
        'end_date': date(2023, 6, 30),
        'featured': True,
        'order': 1,
        'demo_url': 'https://example-ecommerce.com',
        'github_url': 'https://github.com/username/ecommerce',
    },
    {
        'title': 'Task Management App',
        'slug': 'task-management-app',
        'description': 'A collaborative task management application with real-time updates.',
        'long_description': 'Built a task management application allowing teams to collaborate on projects. Features include task creation, assignment, progress tracking, comments, and file attachments. Implemented WebSocket for real-time updates.',
        'technologies': 'Django REST, React, WebSocket, MongoDB, Docker',
        'start_date': date(2023, 7, 1),
        'end_date': date(2023, 10, 15),
        'featured': True,
        'order': 2,
        'demo_url': 'https://example-tasks.com',
        'github_url': 'https://github.com/username/task-app',
    },
    {
        'title': 'Data Analytics Dashboard',
        'slug': 'data-analytics-dashboard',
        'description': 'An interactive data visualization dashboard for business analytics.',
        'long_description': 'Created an advanced analytics dashboard that visualizes business metrics and KPIs. Includes interactive charts, real-time data updates, custom reporting, and data export functionality.',
        'technologies': 'Django, Vue.js, Chart.js, PostgreSQL, Redis',
        'start_date': date(2023, 11, 1),
        'end_date': None,  # Ongoing
        'featured': True,
        'order': 3,
        'demo_url': 'https://example-analytics.com',
        'github_url': 'https://github.com/username/analytics',
    },
    {
        'title': 'Weather App',
        'slug': 'weather-app',
        'description': 'A modern weather application with real-time weather data.',
        'long_description': 'Developed a weather application that provides real-time weather updates, forecasts, and severe weather alerts. Built with a clean, intuitive UI and responsive design.',
        'technologies': 'React, OpenWeather API, Tailwind CSS, Node.js',
        'start_date': date(2023, 3, 1),
        'end_date': date(2023, 4, 15),
        'featured': False,
        'order': 4,
        'demo_url': 'https://example-weather.com',
        'github_url': 'https://github.com/username/weather',
    },
    {
        'title': 'Blog Platform',
        'slug': 'blog-platform',
        'description': 'A feature-rich blogging platform with markdown support.',
        'long_description': 'Built a blogging platform with markdown editor, syntax highlighting, comments, and social sharing. Includes SEO optimization and performance analytics.',
        'technologies': 'Django, PostgreSQL, Vue.js, Elasticsearch',
        'start_date': date(2022, 9, 1),
        'end_date': date(2022, 12, 31),
        'featured': False,
        'order': 5,
        'demo_url': 'https://example-blog.com',
        'github_url': 'https://github.com/username/blog',
    },
]

projects_created = 0
for project_data in projects_data:
    project, created = Project.objects.get_or_create(
        slug=project_data['slug'],
        defaults=project_data
    )
    if created:
        projects_created += 1

print(f'✓ {projects_created} projects created successfully')

# ============================================================================
# Create Timeline Entries
# ============================================================================

timeline_data = [
    {
        'title': 'Senior Full Stack Developer',
        'entry_type': 'experience',
        'organization': 'Tech Solutions Inc.',
        'description': 'Leading a team of developers in building scalable web applications. Responsible for architecture decisions, code reviews, and mentoring junior developers.',
        'start_date': date(2023, 1, 1),
        'end_date': None,
        'icon': '💼',
        'order': 1,
    },
    {
        'title': 'Full Stack Developer',
        'entry_type': 'experience',
        'organization': 'Digital Innovations LLC',
        'description': 'Developed and maintained multiple web applications. Worked with Django, React, and PostgreSQL. Implemented RESTful APIs and optimized database queries.',
        'start_date': date(2021, 6, 1),
        'end_date': date(2022, 12, 31),
        'icon': '💻',
        'order': 2,
    },
    {
        'title': 'Bachelor of Science in Computer Science',
        'entry_type': 'education',
        'organization': 'State University',
        'description': 'Graduated with honors. Focused on web development, database design, and software engineering principles.',
        'start_date': date(2017, 9, 1),
        'end_date': date(2021, 5, 31),
        'icon': '🎓',
        'order': 3,
    },
    {
        'title': 'AWS Solutions Architect Certification',
        'entry_type': 'achievement',
        'organization': 'Amazon Web Services',
        'description': 'Achieved AWS Solutions Architect - Professional certification, demonstrating expertise in designing scalable and resilient applications on AWS.',
        'start_date': date(2023, 5, 15),
        'end_date': None,
        'icon': '🏆',
        'order': 4,
    },
    {
        'title': 'Django & REST API Mastery Course',
        'entry_type': 'achievement',
        'organization': 'Udemy / Online Learning Platform',
        'description': 'Completed comprehensive course on Django framework and REST API development with real-world projects.',
        'start_date': date(2022, 3, 1),
        'end_date': date(2022, 6, 30),
        'icon': '📚',
        'order': 5,
    },
]

timeline_created = 0
for entry_data in timeline_data:
    entry, created = TimelineEntry.objects.get_or_create(
        title=entry_data['title'],
        start_date=entry_data['start_date'],
        defaults=entry_data
    )
    if created:
        timeline_created += 1

print(f'✓ {timeline_created} timeline entries created successfully')

# ============================================================================
# Summary
# ============================================================================

print('\n' + '='*50)
print('Sample Data Population Complete!')
print('='*50)
print(f'Profile: 1')
print(f'Skills: {skills_created}')
print(f'Projects: {projects_created}')
print(f'Timeline Entries: {timeline_created}')
print('\nNext steps:')
print('1. Go to http://localhost:8000/admin')
print('2. Login with your superuser credentials')
print('3. Review and customize the data')
print('4. Visit http://localhost:8000 to see the portfolio')
