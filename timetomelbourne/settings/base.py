# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from celery.schedules import crontab

from django.core.exceptions import ImproperlyConfigured

def get_env_variable(var_name):
    """Get the env var or return an exception"""
    try:
        return os.environ[var_name]
    except KeyError:
        error_message = "Set the {} environment variable".format(var_name)
        raise ImproperlyConfigured(error_message)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_env_variable("SECRET_KEY")

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'djgeojson',
    'leaflet',
    'pttime'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'timetomelbourne.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'timetomelbourne.wsgi.application'


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Australia/Melbourne'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'


# Django Leaflet stuff

LEAFLET_CONFIG = {
    'DEFAULT_CENTER': (144.9629044532776, -37.81044510305556),
    'DEFAULT_ZOOM': 12,
    'MIN_ZOOM': 4,
    'MAX_ZOOM': 20,
    'TILES': 'http://192.168.56.101/osm/{z}/{x}/{y}.png',
    'NO_GLOBALS': False,
    'PLUGINS': {
        'forms': {
                'js': ['/static/pttime/jquery-2.1.4.js', '/static/pttime/admin-point.js'],
                'auto-include': True,
        },
    }
    # 'SPATIAL_EXTENT': (5.0, 44.0, 7.5, 46)
}


# LOGGING!

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'debug.log',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },

}

BINGMAPS = {
    'key': 'Ag3rJe-YpHuknwoKRjZooOoTldyyukufpqLQuyu8VfdXnuqRC7SI30sWMoLtG6bh',
    'url': 'http://dev.virtualearth.net/REST/V1/'
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': '/var/tmp/django_cache',
    }
}

# commented this out as it was causing a circular dependancy
#from pttime.tasks import load_route
# Celery shit
CELERYBEAT_SCHEDULE = {
    # Executes every minute
    'route-load-every-minute': {
        'task': 'pttime.tasks.load_route',
        'schedule': crontab()
    },
}
