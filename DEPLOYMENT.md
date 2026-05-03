# Production Deployment Guide

This guide covers deploying the Digital Identity Hub to production environments.

## 📋 Pre-Deployment Checklist

- [ ] DEBUG = False in settings.py
- [ ] SECRET_KEY is strong and private
- [ ] ALLOWED_HOSTS configured for your domain
- [ ] Database migrated
- [ ] Static files collected
- [ ] Media files uploaded
- [ ] Backups created
- [ ] HTTPS/SSL certificate obtained
- [ ] Monitoring/logging configured

## 🌐 Deployment Options

### Option 1: Heroku (Easiest)

#### Prerequisites
- Heroku account (free tier available)
- Heroku CLI installed
- Git installed

#### Steps

1. **Create Procfile** in project root:
```
web: gunicorn digital_identity_hub.wsgi
```

2. **Create runtime.txt** in project root:
```
python-3.11.4
```

3. **Update requirements.txt**:
```bash
pip install gunicorn
pip freeze > requirements.txt
```

4. **Configure production settings** - Create `settings_production.py` or use environment variables:
```python
import os

DEBUG = False
ALLOWED_HOSTS = ['yourdomain.herokuapp.com']
SECRET_KEY = os.environ.get('SECRET_KEY')

# Database - Heroku provides DATABASE_URL
import dj_database_url
DATABASES = {
    'default': dj_database_url.config(default='sqlite:///db.sqlite3')
}

# Static files
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
```

5. **Deploy to Heroku**:
```bash
# Login to Heroku
heroku login

# Create Heroku app
heroku create your-app-name

# Set environment variables
heroku config:set SECRET_KEY='your-secret-key'

# Push to Heroku
git push heroku main

# Run migrations
heroku run python manage.py migrate

# Create superuser
heroku run python manage.py createsuperuser

# View logs
heroku logs --tail
```

### Option 2: PythonAnywhere

#### Prerequisites
- PythonAnywhere account
- Uploaded project files
- Web app configured

#### Steps

1. **Upload project files** via Web interface or Git

2. **Create virtual environment**:
```bash
mkvirtualenv --python=/usr/bin/python3.10 digital_identity_hub
pip install -r requirements.txt
```

3. **Configure web app** in PythonAnywhere dashboard:
   - Source code: `/home/username/digital_identity_hub`
   - WSGI file: Configure to use your project's wsgi.py

4. **Set environment variables** in WSGI file:
```python
os.environ.setdefault('SECRET_KEY', 'your-secret-key')
os.environ.setdefault('DEBUG', 'False')
```

5. **Reload web app** and visit your domain

### Option 3: DigitalOcean App Platform

#### Prerequisites
- DigitalOcean account
- Project on GitHub
- App Platform enabled

#### Steps

1. **Push project to GitHub**

2. **In DigitalOcean dashboard**:
   - Create App Platform app
   - Connect GitHub repository
   - Set build and run commands:
     ```
     Build: pip install -r requirements.txt
     Run: gunicorn digital_identity_hub.wsgi
     ```

3. **Set environment variables**:
   - SECRET_KEY
   - DEBUG = False
   - ALLOWED_HOSTS

4. **Deploy and monitor**

### Option 4: AWS EC2

#### Prerequisites
- AWS account
- EC2 instance (Ubuntu 20.04 recommended)
- SSH access to instance

#### Steps

1. **SSH into instance**:
```bash
ssh -i your-key.pem ubuntu@your-instance-ip
```

2. **Install dependencies**:
```bash
sudo apt update
sudo apt install python3-pip python3-venv postgresql nginx
```

3. **Clone project**:
```bash
git clone your-repository.git
cd digital_identity_hub
```

4. **Create virtual environment**:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install gunicorn
```

5. **Configure PostgreSQL**:
```bash
sudo -u postgres psql
CREATE DATABASE portfolio_db;
CREATE USER portfolio_user WITH PASSWORD 'strong-password';
ALTER ROLE portfolio_user SET client_encoding TO 'utf8';
ALTER ROLE portfolio_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE portfolio_user SET default_transaction_deferrable TO on;
ALTER ROLE portfolio_user SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE portfolio_db TO portfolio_user;
\q
```

6. **Update settings.py**:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'portfolio_db',
        'USER': 'portfolio_user',
        'PASSWORD': 'strong-password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

7. **Run migrations**:
```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py collectstatic --noinput
```

8. **Create systemd service** - Create `/etc/systemd/system/django.service`:
```ini
[Unit]
Description=Digital Identity Hub Django Service
After=network.target

[Service]
User=www-data
Group=www-data
WorkingDirectory=/home/ubuntu/digital_identity_hub
ExecStart=/home/ubuntu/digital_identity_hub/venv/bin/gunicorn \
          --workers 3 \
          --bind unix:/run/gunicorn.sock \
          digital_identity_hub.wsgi:application

[Install]
WantedBy=multi-user.target
```

9. **Configure Nginx** - Create `/etc/nginx/sites-available/default`:
```nginx
upstream django {
    server unix:/run/gunicorn.sock;
}

server {
    listen 80;
    server_name your-domain.com;

    location /static/ {
        alias /home/ubuntu/digital_identity_hub/staticfiles/;
    }

    location /media/ {
        alias /home/ubuntu/digital_identity_hub/media/;
    }

    location / {
        proxy_pass http://django;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

10. **Enable HTTPS** with Let's Encrypt:
```bash
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d your-domain.com
```

## 🔐 Security Hardening

### Update settings.py for Production

```python
# Security settings
DEBUG = False
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'
SECURE_CONTENT_SECURITY_POLICY = {
    'default-src': ("'self'",),
    'script-src': ("'self'", "'unsafe-inline'"),
}

# Use environment variables for sensitive data
SECRET_KEY = os.environ.get('SECRET_KEY')
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '').split(',')

# Database
DATABASES = {
    'default': dj_database_url.config()
}
```

### Environment Variables

Create `.env` file (never commit this):
```
SECRET_KEY=your-super-secret-key-here
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
DATABASE_URL=postgresql://user:pass@host:5432/dbname
STATIC_ROOT=/var/www/static/
MEDIA_ROOT=/var/www/media/
```

Load with `python-dotenv`:
```bash
pip install python-dotenv
```

In settings.py:
```python
from dotenv import load_dotenv
load_dotenv()
```

## 📊 Monitoring & Logging

### Setup Logging

```python
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': '/var/log/django/app.log',
            'formatter': 'verbose',
        },
    },
    'root': {
        'handlers': ['file'],
        'level': 'INFO',
    },
}
```

### Monitor Performance

```bash
# Install monitoring tools
pip install django-extensions
pip install django-debug-toolbar

# Monitor with New Relic, Sentry, etc.
pip install sentry-sdk
pip install newrelic
```

## 🔄 Backup & Recovery

### Database Backups

```bash
# Backup PostgreSQL
pg_dump portfolio_db > backup.sql

# Backup all data
python manage.py dumpdata > backup.json

# Restore from backup
psql portfolio_db < backup.sql
python manage.py loaddata backup.json
```

### Automated Backups

Create `backup.sh`:
```bash
#!/bin/bash
DATE=$(date +%Y%m%d_%H%M%S)
BACKUP_DIR="/backups"

# Backup database
pg_dump portfolio_db > $BACKUP_DIR/db_$DATE.sql

# Backup Django data
python manage.py dumpdata > $BACKUP_DIR/data_$DATE.json

# Backup media files
tar -czf $BACKUP_DIR/media_$DATE.tar.gz /home/ubuntu/digital_identity_hub/media/
```

Schedule with cron:
```bash
0 2 * * * /home/ubuntu/backup.sh  # Daily at 2 AM
```

## 🚀 Performance Optimization

### Caching

```python
# Redis caching
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
    }
}
```

### Database Optimization

```python
# In views.py - Use select_related for ForeignKey
projects = Project.objects.select_related('category').all()

# Use prefetch_related for M2M/reverse
skills = Skill.objects.prefetch_related('projects').all()
```

### Static Files

```python
# Use whitenoise for static files
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Configure CDN
STATIC_URL = 'https://cdn.yourdomain.com/static/'
```

## ✅ Post-Deployment

1. **Verify site is working**: Visit your domain
2. **Test admin panel**: Login and check data
3. **Check security**: Run security checks
4. **Monitor logs**: Check for errors
5. **Test contact form**: Ensure it works
6. **Test on mobile**: Verify responsiveness
7. **Check performance**: Use GTmetrix or PageSpeed

## 📝 Maintenance

### Regular Tasks

```bash
# Clear cache
python manage.py clear_cache

# Update packages
pip install --upgrade -r requirements.txt

# Check for security issues
pip-audit

# Backup database
python manage.py dumpdata > backup.json
```

### Scheduled Tasks

Setup with Celery or APScheduler:
```bash
pip install celery
pip install django-beat
```

## 🆘 Troubleshooting Production

### App won't start

1. Check logs: `heroku logs --tail`
2. Verify settings: `python manage.py check`
3. Verify environment variables are set
4. Check database connection

### Static files not loading

```bash
python manage.py collectstatic --noinput
```

### Database migrations failing

```bash
python manage.py migrate --dry-run
python manage.py migrate --verbosity 3
```

### High server load

1. Check for slow queries
2. Enable caching
3. Optimize database queries
4. Consider load balancing

## 📚 Resources

- [Django Deployment](https://docs.djangoproject.com/en/4.2/howto/deployment/)
- [Heroku Django Docs](https://devcenter.heroku.com/articles/django-app-configuration)
- [AWS EC2 Django](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-django.html)
- [DigitalOcean Guides](https://www.digitalocean.com/community/tutorials?q=django)

---

**Congratulations on deploying your portfolio! 🎉**

Remember: Always test in staging before deploying to production!
