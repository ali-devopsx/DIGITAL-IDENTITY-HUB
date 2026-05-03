# Troubleshooting Guide

This guide covers common issues and their solutions.

## 🔴 Installation Issues

### Issue: "ModuleNotFoundError: No module named 'django'"

**Solution:**
```bash
# Make sure virtual environment is activated
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Then install dependencies
pip install -r requirements.txt
```

### Issue: "Python is not recognized"

**Solution:**
- Python is not installed or not in PATH
- Install Python from: https://www.python.org
- During installation, **check "Add Python to PATH"**
- Restart your terminal after installing

### Issue: "pip: command not found"

**Solution:**
```bash
# Try using python directly
python -m pip install -r requirements.txt

# Or upgrade pip
python -m pip install --upgrade pip
```

### Issue: "ModuleNotFoundError: No module named 'PIL'"

**Solution:**
```bash
pip install Pillow
```

## 🔴 Database Issues

### Issue: "no such table: core_profile"

**Solution:**
```bash
# Run migrations
python manage.py migrate

# If that doesn't work, reset database (WARNING: deletes all data)
rm db.sqlite3  # On macOS/Linux: rm db.sqlite3
del db.sqlite3  # On Windows
python manage.py migrate
```

### Issue: "django.db.utils.OperationalError: database is locked"

**Solution:**
- Stop the running server
- Delete the database file: `db.sqlite3`
- Run migrations again: `python manage.py migrate`
- Restart the server

## 🔴 Server Issues

### Issue: "Port 8000 already in use"

**Solution:**
```bash
# Use a different port
python manage.py runserver 8001

# Or kill the process using port 8000
# On Windows:
netstat -ano | findstr :8000
taskkill /PID <PID> /F

# On macOS/Linux:
lsof -ti:8000 | xargs kill -9
```

### Issue: "DisallowedHost at / - Invalid HTTP_HOST header"

**Solution:**
Edit `digital_identity_hub/settings.py`:
```python
ALLOWED_HOSTS = ['*']  # For development only
# Or specify your domain:
ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'yourdomain.com']
```

## 🔴 Static Files Issues

### Issue: "CSS and JavaScript not loading"

**Solution:**
```bash
# Collect static files
python manage.py collectstatic

# In development, make sure DEBUG = True in settings.py
# Check that STATIC_URL = '/static/' and STATIC_ROOT is set
```

### Issue: "Images not displaying"

**Solution:**
1. Check that image was uploaded: `media/` folder should exist
2. Verify `MEDIA_URL` and `MEDIA_ROOT` in `settings.py`
3. For development, Django should serve media files automatically
4. Ensure `DEBUG = True` in settings.py

## 🔴 Admin Panel Issues

### Issue: "Admin login page shows but credentials don't work"

**Solution:**
```bash
# Create a new superuser
python manage.py createsuperuser
```

### Issue: "No such table: auth_user"

**Solution:**
```bash
# Run migrations to create auth tables
python manage.py migrate
```

### Issue: "Models not showing in admin"

**Solution:**
Check `core/admin.py` - make sure models are registered:
```python
from django.contrib import admin
from .models import Profile, Skill, Project, TimelineEntry, Contact

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass

# ... repeat for other models
```

## 🔴 Template Issues

### Issue: "TemplateDoesNotExist at /"

**Solution:**
1. Check that `templates/` folder exists
2. Check that `TEMPLATES` setting in `settings.py` includes your path:
```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Make sure this is set
        'APP_DIRS': True,
        # ...
    },
]
```

### Issue: "Template variables not showing"

**Solution:**
1. Check view passes correct context:
```python
context = {
    'profile': profile,
    'skills': skills,
}
return render(request, 'core/index.html', context)
```

2. Check template variable syntax: `{{ variable_name }}`
3. Check for typos in variable names

## 🔴 Form Issues

### Issue: "CSRF token missing or incorrect"

**Solution:**
1. Make sure form includes CSRF token:
```html
<form method="POST">
    {% csrf_token %}
    <!-- form fields -->
</form>
```

2. Check CSRF middleware is installed in `settings.py`:
```python
MIDDLEWARE = [
    # ...
    'django.middleware.csrf.CsrfViewMiddleware',
    # ...
]
```

### Issue: "Contact form not working / not sending"

**Solution:**
```bash
# Check Django shell for errors
python manage.py shell

# Test contact model
from core.models import Contact
Contact.objects.all()  # Check if submissions are saved

# Exit shell
exit()
```

## 🔴 JavaScript Issues

### Issue: "Typing animation not working"

**Solution:**
1. Check `static/js/main.js` is loaded in template
2. Open browser DevTools (F12) - check Console tab for errors
3. Verify element with id "typing" exists in HTML
4. Check browser console for error messages

### Issue: "Navigation menu not working on mobile"

**Solution:**
1. Check hamburger button is visible on mobile
2. Verify CSS media queries are working
3. Check JavaScript event listeners are attached
4. Open DevTools and test with device toolbar

## 🔴 Contact Form Issues

### Issue: "Form submission shows error"

**Solution:**
1. Check browser console (F12) for JavaScript errors
2. Check Django console for Python errors
3. Verify form fields match model fields
4. Check Django admin - are messages being saved?

### Issue: "Email notifications not sending"

**Solution:**
Email is commented out by default. To enable:

1. In `core/views.py`, uncomment the email code:
```python
# Uncomment the email sending code
```

2. Configure email in `settings.py`:
```python
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'  # For development
# For production, use your email service
```

## 🔴 Responsive Design Issues

### Issue: "Site not responsive on mobile"

**Solution:**
1. Check `<meta name="viewport">` in template
2. Verify CSS media queries are working
3. Test with browser DevTools device toolbar
4. Check for hardcoded pixel values that don't adapt

### Issue: "Layout breaks on certain screen size"

**Solution:**
1. Check media queries in `style.css`
2. Use browser DevTools to find which breakpoint is failing
3. Adjust CSS for that breakpoint
4. Test on multiple devices

## 🟡 Performance Issues

### Issue: "Page loading slowly"

**Solution:**
```bash
# In development, enable Debug Toolbar (optional)
pip install django-debug-toolbar

# Optimize images
# Use image compression tools for media files

# Minify CSS and JavaScript
# Use tools like cssnano and UglifyJS
```

### Issue: "High database queries"

**Solution:**
```bash
# Install Django Debug Toolbar
pip install django-debug-toolbar

# In development, check query count
# Optimize with select_related() and prefetch_related()
```

## 🟡 Security Issues

### Issue: "SECRET_KEY warning"

**Solution:**
Generate a new SECRET_KEY:
```python
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```

Then update `settings.py` (for production):
```python
SECRET_KEY = 'your-new-generated-key'
# Better: use environment variables
SECRET_KEY = os.environ.get('SECRET_KEY', 'fallback-key')
```

### Issue: "ALLOWED_HOSTS error in production"

**Solution:**
Update `settings.py`:
```python
ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']
```

## 📋 Verification Checklist

If you're having multiple issues, run through this checklist:

- [ ] Python 3.8+ installed
- [ ] Virtual environment activated
- [ ] Dependencies installed: `pip install -r requirements.txt`
- [ ] Database migrated: `python manage.py migrate`
- [ ] Superuser created: `python manage.py createsuperuser`
- [ ] DEBUG = True in settings.py (for development)
- [ ] Static files configured
- [ ] Templates folder configured
- [ ] No syntax errors in Python files
- [ ] No syntax errors in JavaScript files
- [ ] Server running: `python manage.py runserver`

## 🔍 Debug Tools

### Check Python Syntax
```bash
python -m py_compile filename.py
```

### Check Django Configuration
```bash
python manage.py check
```

### View Database Queries
```python
# In Django shell
from django.db import connection
from django.db.backends import utils
print(connection.queries)
```

### Test Views Directly
```python
# In Django shell
from django.test import Client
client = Client()
response = client.get('/')
print(response.status_code)
print(response.content)
```

## 📞 Getting More Help

1. **Django Documentation**: https://docs.djangoproject.com/
2. **Stack Overflow**: Tag questions with `django`
3. **Django Community Forum**: https://forum.djangoproject.com/
4. **Django Discord**: https://discord.gg/django

## 🎯 Still Having Issues?

1. **Run verification script**: `python verify_setup.py`
2. **Check error messages carefully** - they usually indicate the problem
3. **Search online** - your error is likely common
4. **Post on Stack Overflow** with full error message and code
5. **Check project files** - make sure they weren't accidentally modified

---

Remember: Always backup your database before making major changes!

```bash
python manage.py dumpdata > backup.json
```

Good luck! 🚀
