from pathlib import Path
import os
import dj_database_url

# BASE_DIR の設定
BASE_DIR = Path(__file__).resolve().parent.parent

# SECRET_KEY の取得
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'your-default-secret-key')

# DEBUG の設定
DEBUG = os.getenv('DJANGO_DEBUG', 'False').lower() == 'true'

# 許可するホスト
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '127.0.0.1,localhost,skm-sk-tokyo-net.herokuapp.com').split(',')

# アプリケーション
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django_browser_reload',
    'bms',
    'attendance',
    'accounts',
    'inventory',
    'customers',
    'docspdf',
    'core',
    'notifications',
]

# ミドルウェア
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

# URL 設定
ROOT_URLCONF = 'bms.urls'

# テンプレート設定
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'bms.context_processors.profile_info',
            ],
        },
    },
]

# メール設定
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# WSGI設定
WSGI_APPLICATION = 'bms.wsgi.application'

# データベース設定
DATABASES = {
    'default': dj_database_url.config(default=os.getenv('DATABASE_URL', ''))
}

if not DATABASES['default']:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.getenv('DB_NAME', 'skm'),
            'USER': os.getenv('DB_USER', 'skmaster'),
            'PASSWORD': os.getenv('DB_PASSWORD', 'sktokyo031114'),
            'HOST': os.getenv('DB_HOST', 'localhost'),
            'PORT': os.getenv('DB_PORT', '5432'),
        }
    }

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# 静的ファイル設定
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# メディア設定
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# ログイン関連
LOGIN_REDIRECT_URL = '/mypage/'
LOGIN_URL = '/login/'

# ロギング設定
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/debug.log'),
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

# logsディレクトリ作成
log_dir = BASE_DIR / 'logs'
os.makedirs(log_dir, exist_ok=True)

LANGUAGE_CODE = 'ja'
