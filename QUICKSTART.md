# Digital Identity Hub - Quick Start Guide

Welcome! This guide will help you get started with the Digital Identity Hub project in minutes.

## ⚡ Quick Setup (5 minutes)

### Option 1: Automated Setup (Recommended)

**For Windows:**
```bash
setup.bat
```

**For macOS/Linux:**
```bash
bash setup.sh
```

### Option 2: Manual Setup

#### Step 1: Create Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

#### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

#### Step 3: Create Database
```bash
python manage.py migrate
```

#### Step 4: Create Admin User
```bash
python manage.py createsuperuser
# Follow prompts to create username and password
```

#### Step 5: Populate Sample Data (Optional)
```bash
python manage.py shell
# Then in the shell:
exec(open('populate_sample_data.py').read())
# Then exit: exit()
```

#### Step 6: Start Server
```bash
python manage.py runserver
```

## 🌐 Access the Site

- **Homepage**: http://localhost:8000
- **Admin Panel**: http://localhost:8000/admin

## 📝 First Things to Do

### 1. Update Your Profile

1. Go to http://localhost:8000/admin
2. Login with your superuser credentials
3. Click on "Profile" 
4. Fill in your information:
   - Name
   - Title/Role
   - Bio
   - Contact information
   - Social media links
   - Upload a profile image

### 2. Add Your Skills

1. In admin, click "Skills"
2. Click "Add Skill"
3. Fill in:
   - Skill name (e.g., "Python", "React")
   - Category (Frontend, Backend, Database, Tools, Soft Skills)
   - Proficiency level
   - Icon/emoji (optional)
   - Order (for sorting)

### 3. Add Your Projects

1. In admin, click "Projects"
2. Click "Add Project"
3. Fill in project details:
   - Title and description
   - Technologies used
   - Start date and end date
   - Links to demo and GitHub
   - Upload project image
   - Mark as "Featured" to show on homepage

### 4. Add Timeline Entries

1. In admin, click "Timeline Entries"
2. Click "Add Timeline Entry"
3. Add your career/education history:
   - Title (job title, degree name, etc.)
   - Type (Education, Experience, Achievement)
   - Organization name
   - Dates
   - Description

## 🎨 Customizing the Site

### Change the Color Scheme

Edit `static/css/style.css` and modify the CSS variables at the top:

```css
:root {
    --primary-bg: #0a0e27;      /* Change main background */
    --accent-color: #00ff88;    /* Change accent color */
    --accent-alt: #ff006e;      /* Change alternative accent */
}
```

### Popular Color Combinations

**Purple & Pink:**
```css
--primary-bg: #1a0033;
--accent-color: #cc00ff;
--accent-alt: #ff0099;
```

**Dark Blue & Cyan:**
```css
--primary-bg: #0d1b2a;
--accent-color: #00d9ff;
--accent-alt: #0099ff;
```

**Green & Teal:**
```css
--primary-bg: #0a1f12;
--accent-color: #00ff88;
--accent-alt: #00cc99;
```

### Add Your Own Image

1. In Admin > Profile
2. Upload a profile image
3. The image will appear in the hero section

## 🚀 Deploying to Production

### Using Heroku

1. Install Heroku CLI
2. Create `Procfile`:
   ```
   web: gunicorn digital_identity_hub.wsgi
   ```

3. Create `runtime.txt`:
   ```
   python-3.11.4
   ```

4. Deploy:
   ```bash
   heroku create your-app-name
   git push heroku main
   heroku run python manage.py migrate
   heroku run python manage.py createsuperuser
   ```

### Using PythonAnywhere

1. Upload files to PythonAnywhere
2. Create virtual environment
3. Install requirements
4. Configure Django settings
5. Reload app

## 🔧 Common Commands

```bash
# Run development server
python manage.py runserver

# Create migrations after changing models
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create admin user
python manage.py createsuperuser

# Collect static files
python manage.py collectstatic

# Enter Django shell
python manage.py shell

# Run tests
python manage.py test

# Create backup
python manage.py dumpdata > backup.json

# Restore from backup
python manage.py loaddata backup.json
```

## 📚 Project File Locations

| File | Purpose |
|------|---------|
| `manage.py` | Django command-line tool |
| `settings.py` | Project configuration |
| `urls.py` | URL routing |
| `models.py` | Database models |
| `views.py` | View logic |
| `admin.py` | Admin configuration |
| `templates/core/index.html` | Homepage template |
| `static/css/style.css` | Styling |
| `static/js/main.js` | JavaScript |

## 🐛 Troubleshooting

### "Port 8000 already in use"
```bash
python manage.py runserver 8001
```

### "Image upload not working"
```bash
pip install Pillow
python manage.py migrate
```

### "Static files not showing"
```bash
python manage.py collectstatic
```

### "Database error"
```bash
python manage.py migrate
```

## 💡 Tips & Tricks

1. **Use Django Shell to test**: `python manage.py shell`
2. **Check logs for errors**: Look at the terminal output
3. **Use admin to manage content**: Don't edit database files directly
4. **Backup before major changes**: `python manage.py dumpdata > backup.json`
5. **Test on different devices**: Use phone/tablet to check responsiveness

## 🎓 Learning Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [HTML/CSS Tutorial](https://www.w3schools.com/)
- [JavaScript Tutorial](https://javascript.info/)
- [Django Models](https://docs.djangoproject.com/en/4.2/topics/db/models/)

## 📞 Need Help?

1. Check the README.md for detailed documentation
2. Read the comments in the code files
3. Check Django documentation
4. Review the troubleshooting section

## 🎉 Next Steps

1. ✅ Setup complete
2. ✅ Create admin user
3. ✅ Update your profile
4. ✅ Add your skills, projects, and timeline
5. ✅ Customize colors and content
6. 🚀 Deploy to production

Good luck with your portfolio! 🚀
