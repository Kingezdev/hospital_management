# Hospital Management App - Render Deployment Guide

## Overview
This guide covers deploying the Hospital Management Django application to Render.com.

## Prerequisites
- GitHub repository with the code
- Render.com account
- PostgreSQL database (Render provides this)

## Deployment Steps

### 1. Prepare Your Repository
- Ensure all code is pushed to GitHub
- Verify the `.gitignore` file excludes sensitive files
- Confirm `requirements.txt` includes all dependencies

### 2. Create Render Services

#### Web Service
1. Go to Render.com dashboard
2. Click "New" → "Web Service"
3. Connect your GitHub repository
4. Configure:
   - **Name**: hospital-management-web
   - **Runtime**: Python
   - **Build Command**: `pip install -r requirements.txt && python manage.py collectstatic --noinput`
   - **Start Command**: `gunicorn core.wsgi:application`
   - **Environment Variables**:
     - `DEBUG`: `false`
     - `SECRET_KEY`: Generate automatically
     - `DJANGO_SETTINGS_MODULE`: `core.settings.production`

#### PostgreSQL Database
1. Click "New" → "PostgreSQL"
2. Configure:
   - **Name**: hospital-management-db
   - **Plan**: Free tier
   - **Region**: Choose nearest region

### 3. Environment Variables
Set these in your web service:

#### Required
```
DEBUG=False
SECRET_KEY=your-generated-secret-key
DJANGO_SETTINGS_MODULE=core.settings.production
DATABASE_URL=postgresql://username:password@host:port/database
```

#### Optional (for email)
```
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
```

### 4. Database Migration
After deployment, run migrations:
1. Go to your web service → "Shell"
2. Run: `python manage.py migrate`
3. Create superuser: `python manage.py createsuperuser`

### 5. Static Files
Static files are automatically collected during build with:
```
python manage.py collectstatic --noinput
```

## Configuration Files

### render.yaml
Automatically configures services when connected to Render.

### Procfile
Defines how to run the web application with Gunicorn.

### production.py
Production-specific Django settings including:
- Security configurations
- Database connections
- Static file serving
- Logging setup

## Post-Deployment Checklist

1. **Test the application**
   - Visit the provided URL
   - Test user registration/login
   - Verify all pages load correctly

2. **Check admin panel**
   - Access `/admin/`
   - Verify database models are accessible

3. **Test mobile responsiveness**
   - Test on mobile devices
   - Verify navigation works correctly

4. **Monitor logs**
   - Check Render logs for any errors
   - Monitor application performance

## Troubleshooting

### Common Issues

#### 1. Database Connection Error
- Verify `DATABASE_URL` is correctly set
- Check if database is running
- Ensure migrations are applied

#### 2. Static Files Not Loading
- Verify `collectstatic` ran during build
- Check `STATIC_URL` and `STATIC_ROOT` settings
- Ensure Whitenoise is properly configured

#### 3. 500 Internal Server Error
- Check Render logs for specific error
- Verify environment variables
- Ensure all dependencies are installed

#### 4. Permission Denied Errors
- Check file permissions in production
- Verify database user has correct privileges

## Performance Optimization

### 1. Database Optimization
- Use connection pooling
- Add database indexes
- Optimize queries

### 2. Caching
- Enable Redis caching
- Cache static assets
- Use browser caching headers

### 3. Static Files
- Use CDN for static files
- Compress images and assets
- Enable gzip compression

## Security Considerations

1. **Environment Variables**: Never commit secrets to git
2. **HTTPS**: Enable SSL/TLS (Render provides this)
3. **Database Security**: Use strong passwords
4. **Regular Updates**: Keep dependencies updated
5. **Backup Strategy**: Regular database backups

## Scaling Up

When ready to scale:
1. Upgrade to paid Render plans
2. Add Redis for session storage
3. Use CDN for static files
4. Implement load balancing
5. Monitor performance metrics

## Support

For Render-specific issues:
- Check Render documentation
- Contact Render support
- Review deployment logs

For application issues:
- Check Django error logs
- Verify configuration settings
- Test locally first
