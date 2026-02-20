import os

class Config:
    """Application configuration"""
    
    # Secret key for session management and CSRF protection
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production-2026'
    
    # Database configuration
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    
    # On Vercel, the filesystem is read-only except for /tmp
    if os.environ.get('VERCEL'):
        db_path = os.path.join('/tmp', 'learn_with_ak.db')
    else:
        db_path = os.path.join(BASE_DIR, 'learn_with_ak.db')
        
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + db_path
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Super admin email (hardcoded as per requirements)
    SUPER_ADMIN_EMAIL = 'aryankumar735588@gmail.com'
    
    # Flask-Login settings
    REMEMBER_COOKIE_DURATION = 86400  # 1 day in seconds
    SESSION_PROTECTION = 'strong'

    # Google Gemini API (for AI Roadmap Generator)
    # Key is loaded from .env file — never hardcode secrets here
    GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY', '')
