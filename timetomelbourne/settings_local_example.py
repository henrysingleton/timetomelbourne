# Rename to settings_local.py and customise

#SECRET_KEY = 'MustBeUniquePleaseChange'

#DEBUG = False
#ALLOWED_HOSTS = [ 'domain.name.here' ]

## for production (by default will run sqlite)
## you will need to "pip install mysqlclient" (not installed by default, see requirements.txt)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'timetomelbourne',
        'USER': 'postgres',
        'PASSWORD': 'password',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
#ADMINS = (
#	 ('Admin Name', 'user@example.com'),
#)

# for production only: set below to absolute file system
#   path you configure nginx to serve /static from
#STATIC_ROOT="/home/sites/website/static"


#CACHES = {
#    'default': {
#        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
#    }
#}

#EMAIL_HOST = 'smtp.mandrillapp.com'
#EMAIL_HOST_USER = ''
#EMAIL_HOST_PASSWORD = ''
#EMAIL_PORT = 587
#EMAIL_USE_TLS = True