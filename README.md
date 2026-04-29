# Hospital Management System

A modern, responsive hospital management system built with Django and Bootstrap, featuring a clean UI with mobile-friendly design and comprehensive patient management capabilities.

## 🌟 Features

### Core Functionality
- **User Management**: Role-based authentication (Admin, Doctor, Staff)
- **Patient Management**: Complete patient records and medical history
- **Appointment Scheduling**: Book and manage patient appointments
- **Medical Records**: Track illnesses, treatments, and patient progress
- **Dashboard Analytics**: Real-time statistics and insights

### UI/UX Features
- **Modern Design**: Bootstrap 5.3.0 with custom styling
- **Mobile Responsive**: Fully optimized for all device sizes
- **Interactive Navigation**: Collapsible mobile menu with smooth animations
- **Touch-Friendly**: Optimized for mobile interactions
- **Dark Sidebar**: Professional navigation with icon-based menu

### Technical Features
- **Django 4.2**: Robust backend framework
- **PostgreSQL**: Scalable database solution
- **Redis Caching**: Performance optimization
- **Gunicorn**: Production-ready WSGI server
- **Whitenoise**: Static file serving

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- PostgreSQL (optional, SQLite for development)
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Kingezdev/hospital_management.git
   cd hospital_management/core
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment setup**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

5. **Database setup**
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```

6. **Run the application**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   - URL: `http://localhost:8000`
   - Admin: `http://localhost:8000/admin/`

### Default Users
- **Admin**: `admin` / `admin123`
- **Doctor**: `doctor` / `doctor123`

## 📱 Mobile Experience

The application is fully optimized for mobile devices with:

- **Responsive Design**: Adapts to all screen sizes
- **Mobile Navigation**: Hamburger menu with slide-out sidebar
- **Touch Interactions**: Large tap targets and smooth animations
- **Mobile Tables**: Card-based layouts for data on small screens
- **Optimized Forms**: Mobile-friendly input fields and buttons

## 🏗️ Project Structure

```
hospital_management/
├── core/                          # Main Django project
│   ├── core/                      # Project settings
│   │   ├── settings/              # Environment-specific settings
│   │   │   ├── base.py          # Base settings
│   │   │   └── production.py    # Production settings
│   │   ├── urls.py              # Main URL configuration
│   │   └── wsgi.py              # WSGI configuration
│   ├── accounts/                 # User management app
│   │   ├── models.py            # Custom user model
│   │   ├── forms.py             # User forms
│   │   └── templatetags/        # Custom template filters
│   ├── medical/                  # Medical management app
│   │   ├── models.py            # Medical models (Patient, Illness, etc.)
│   │   ├── views.py             # Medical views
│   │   └── urls.py              # Medical URLs
│   ├── templates/                # HTML templates
│   │   ├── base.html            # Base template
│   │   ├── accounts/            # Authentication templates
│   │   └── medical/             # Medical app templates
│   └── static/                   # Static files (CSS, JS, images)
├── requirements.txt               # Python dependencies
├── .env                         # Environment variables
├── .gitignore                   # Git ignore file
├── Procfile                     # Heroku/Render deployment
├── render.yaml                  # Render deployment config
└── DEPLOYMENT.md                # Deployment guide
```

## 🎨 UI Components

### Dashboard
- **Statistics Cards**: Patient count, appointments, records
- **Quick Actions**: Easy access to common tasks
- **Recent Activity**: Latest appointments and patient records

### Patient Management
- **Patient List**: Searchable table with mobile card view
- **Patient Forms**: Comprehensive patient information forms
- **Medical History**: Track illnesses and treatments

### Navigation
- **Sidebar Navigation**: Icon-based menu with user info
- **Mobile Menu**: Collapsible hamburger menu
- **Breadcrumb Navigation**: Clear page hierarchy

## 🔧 Configuration

### Environment Variables

Create a `.env` file with the following:

```env
# Django Settings
DEBUG=True
SECRET_KEY=your-secret-key-here
ALLOWED_HOSTS=localhost,127.0.0.1

# Database
DB_NAME=hospital_management
DB_USER=your-username
DB_PASSWORD=your-password
DB_HOST=localhost
DB_PORT=5432

# Email (Optional)
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
```

### Database Setup

#### SQLite (Development)
```bash
# Default configuration, no setup needed
python manage.py migrate
```

#### PostgreSQL (Production)
```bash
# Install PostgreSQL adapter
pip install psycopg2-binary

# Update DATABASE_URL in .env
DATABASE_URL=postgresql://user:password@localhost:5432/dbname
```

## 🚀 Deployment

### Render.com (Recommended)

1. **Push to GitHub**
   ```bash
   git add .
   git commit -m "Ready for deployment"
   git push origin main
   ```

2. **Deploy to Render**
   - Connect your GitHub repository to Render
   - Use the provided `render.yaml` for automatic configuration
   - Set environment variables in Render dashboard

3. **Post-deployment**
   - Run migrations via Render shell
   - Create superuser for admin access

### Manual Deployment

See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed deployment instructions.

## 📊 API Documentation

### User Authentication
- `POST /accounts/login/` - User login
- `POST /accounts/logout/` - User logout
- `POST /accounts/register/` - User registration

### Medical Data
- `GET /medical/patients/` - List patients
- `POST /medical/patients/create/` - Create patient
- `GET /medical/appointments/` - List appointments
- `POST /medical/appointments/create/` - Create appointment

## 🧪 Testing

### Run Tests
```bash
python manage.py test
```

### Test Coverage
```bash
pip install coverage
coverage run --source='.' manage.py test
coverage report
```

## 🛠️ Development

### Code Style
- Follow PEP 8 guidelines
- Use meaningful variable names
- Add comments for complex logic

### Contributing
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

### Common Commands
```bash
# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic

# Create superuser
python manage.py createsuperuser

# Run development server
python manage.py runserver
```

## 🔒 Security

### Features
- **Password Hashing**: Secure password storage
- **CSRF Protection**: Cross-site request forgery protection
- **SQL Injection Prevention**: Django ORM protection
- **XSS Protection**: Cross-site scripting protection
- **HTTPS Support**: SSL/TLS encryption in production

### Best Practices
- Keep dependencies updated
- Use environment variables for secrets
- Enable HTTPS in production
- Regular security audits

## 📈 Performance

### Optimization
- **Database Indexing**: Optimized queries
- **Redis Caching**: Session and data caching
- **Static File Compression**: Reduced load times
- **Image Optimization**: Compressed images

### Monitoring
- **Logging**: Comprehensive error logging
- **Performance Metrics**: Response time tracking
- **Database Queries**: Query optimization

## 🤝 Support

### Documentation
- [Deployment Guide](DEPLOYMENT.md)
- [API Documentation](docs/api.md)
- [Troubleshooting](docs/troubleshooting.md)

### Issues
- Report bugs via GitHub Issues
- Feature requests welcome
- Community support available

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Django Framework
- Bootstrap UI Framework
- Font Awesome Icons
- Render.com for hosting
- Open source community

---

**Built with ❤️ for healthcare professionals**
