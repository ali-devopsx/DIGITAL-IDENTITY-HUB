# Digital Identity Hub

A complete Django-based personal portfolio website with a dynamic identity system. Features a dark cyber aesthetic, smooth animations, and a fully functional admin panel to manage all content.

## 🚀 Features

- **Dynamic Homepage** with animated typing intro
- **Multiple Sections**: About, Skills, Projects, Timeline, Contact
- **Dark Cyber Aesthetic** with smooth animations
- **Fully Responsive Design** - works on all devices
- **Django Admin Panel** - easily manage all content
- **Database-Driven Content** - no hardcoding needed
- **Contact Form** - collect messages from visitors
- **Project Showcase** - display and link your work
- **Timeline** - show your career/education journey
- **Skills Management** - organize and display your expertise

## 📁 Project Structure

```
digital_identity_hub/
├── digital_identity_hub/          # Project configuration
│   ├── __init__.py
│   ├── settings.py               # Django settings
│   ├── urls.py                   # URL routing
│   ├── wsgi.py                   # WSGI configuration
│   └── asgi.py                   # ASGI configuration
│
├── core/                          # Main app
│   ├── migrations/               # Database migrations
│   ├── __init__.py
│   ├── admin.py                  # Admin panel configuration
│   ├── apps.py                   # App configuration
│   ├── models.py                 # Database models
│   ├── urls.py                   # App URL routing
│   └── views.py                  # View logic
│
├── templates/                     # HTML templates
│   └── core/
│       ├── index.html            # Homepage
│       └── project_detail.html   # Project detail page
│
├── static/                        # Static files
│   ├── css/
│   │   └── style.css             # Main stylesheet
│   └── js/
│       └── main.js               # JavaScript
│
├── manage.py                      # Django CLI
├── requirements.txt               # Python dependencies
├── .gitignore                     # Git ignore rules
└── README.md                      # This file
```

## 🛠️ Setup Instructions

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### 1. Create Virtual Environment

```bash
# Navigate to the project directory
cd digital_identity_hub

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Database Setup

```bash
# Create database tables
python manage.py migrate

# Create a superuser (admin account)
python manage.py createsuperuser
# Follow the prompts to create your admin account
```

### 4. Run Development Server

```bash
python manage.py runserver
```

The site will be available at: `http://localhost:8000`

Admin panel: `http://localhost:8000/admin`

## 📝 Database Models

### Profile
- Personal information and bio
- Contact details
- Social media links
- Profile image

### Skill
- Skill name and category
- Proficiency level (Beginner, Intermediate, Advanced, Expert)
- Icon/emoji
- Display order

### Project
- Project title and description
- Technologies used
- Start and end dates
- Links to demo and GitHub
- Featured projects for homepage

### TimelineEntry
- Timeline events (Education, Experience, Achievement)
- Organization name
- Date range
- Description and icon

### Contact
- Store contact form submissions
- Sender information
- Message content
- Read status

## 🎨 Customization

### Add Your Profile Information

1. Go to `http://localhost:8000/admin`
2. Login with your superuser credentials
3. Click on "Profile" and add your information
4. Add skills, projects, and timeline entries

### Customize Colors

Edit `static/css/style.css` and modify CSS variables in `:root`:

```css
:root {
    --primary-bg: #0a0e27;        /* Main background */
    --accent-color: #00ff88;      /* Accent color (neon green) */
    --accent-alt: #ff006e;        /* Alternative accent (pink) */
    /* ... other variables ... */
}
```

### Add New Sections

1. Create a new Django app: `python manage.py startapp new_app`
2. Create models in `new_app/models.py`
3. Register in `new_app/admin.py`
4. Add templates in `templates/new_app/`
5. Create views and URLs

## 🔧 Management Commands

```bash
# Create migrations after changing models
python manage.py makemigrations

# Apply migrations to database
python manage.py migrate

# Create superuser for admin
python manage.py createsuperuser

# Collect static files for production
python manage.py collectstatic

# Run development server
python manage.py runserver

# Run tests
python manage.py test

# Open Django shell
python manage.py shell
```

## 📱 Mobile Responsive

The site is fully responsive with breakpoints at:
- Desktop: 1200px+
- Tablet: 769px - 1199px
- Mobile: Below 768px

Hamburger menu automatically appears on mobile devices.

## 🚀 Production Deployment

### Using Gunicorn

```bash
pip install gunicorn
gunicorn digital_identity_hub.wsgi:application
```

### Important Production Changes

1. **settings.py**:
```python
DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']
SECRET_KEY = os.environ.get('SECRET_KEY')  # Use environment variable
```

2. **Security Settings**:
```python
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 31536000
```

3. **Database**:
```python
# Use PostgreSQL instead of SQLite
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'portfolio_db',
        'USER': 'postgres',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

## 📚 File Explanations

### settings.py
- **Purpose**: Configures Django project
- **Contains**: Database settings, installed apps, middleware, templates
- **Edit**: Add your settings, third-party apps, security options

### models.py
- **Purpose**: Defines database structure
- **Contains**: Profile, Skill, Project, TimelineEntry, Contact models
- **Edit**: Add new fields or models

### views.py
- **Purpose**: Handles business logic
- **Contains**: Homepage view, project detail view, contact form handler
- **Edit**: Modify how data is retrieved and processed

### admin.py
- **Purpose**: Configures Django admin interface
- **Contains**: ModelAdmin classes for all models
- **Edit**: Customize admin display, filtering, search

### templates/core/index.html
- **Purpose**: Homepage template
- **Contains**: Hero section, all portfolio sections, forms
- **Edit**: Modify layout and styling

### static/css/style.css
- **Purpose**: All styling and animations
- **Contains**: Colors, layout, responsive design, animations
- **Edit**: Customize look and feel

### static/js/main.js
- **Purpose**: Client-side interactivity
- **Contains**: Typing animation, form handling, scrolling effects
- **Edit**: Add new interactive features

## 🐛 Troubleshooting

### "ModuleNotFoundError: No module named 'django'"
```bash
pip install -r requirements.txt
```

### "Port 8000 is already in use"
```bash
python manage.py runserver 8001  # Use different port
```

### "Database table does not exist"
```bash
python manage.py migrate
```

### "Image not uploading"
- Make sure Pillow is installed: `pip install Pillow`
- Check `MEDIA_ROOT` and `MEDIA_URL` in settings.py

### "Static files not loading"
```bash
python manage.py collectstatic
```

## 📖 Django Resources

- [Django Official Documentation](https://docs.djangoproject.com/)
- [Django Models](https://docs.djangoproject.com/en/4.2/topics/db/models/)
- [Django Admin](https://docs.djangoproject.com/en/4.2/ref/contrib/admin/)
- [Django Templating](https://docs.djangoproject.com/en/4.2/topics/templates/)

## 🎓 Learning Points

This project demonstrates:
- Django project structure and configuration
- Model design and relationships
- Admin customization
- Template inheritance
- Static file management
- Form handling and AJAX
- Responsive web design
- CSS animations and transitions
- JavaScript for interactivity

## 📄 License

This project is open source and available for personal and commercial use.

## 💡 Future Enhancements

Potential additions:
- Blog functionality
- Resume/CV download
- Dark mode toggle
- Language localization
- SEO optimization
- Comment system on projects
- Analytics integration
- Email notifications

## 🤝 Contributing

Feel free to fork, modify, and improve this project!

## 📞 Support

For issues or questions:
1. Check the troubleshooting section
2. Review Django documentation
3. Check the code comments

## 🎉 Credits

Built with:
- Django
- Vanilla JavaScript
- CSS3 Animations
- Font Awesome Icons

---

**Happy coding! 🚀**

Last Updated: 2024
Version: 1.0.0
