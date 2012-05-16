from django.conf.global_settings import *
import datetime

from letters.functions import rel_path, add_to_middleware

########
#Packages
########
INSTALLED_APPS += (
    'south',
    'grappelli',
  )

GRAPPELLI_ADMIN_TITLE = 'Letters'


########
#Django
########
SITE_ID = 1
DEBUG = True

INSTALLED_APPS += (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',  # required by auth
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.markup',
  )

#Static/Media
STATICFILES_DIRS = (
    ('letters', rel_path('static')),
  )

STATIC_URL = '/static/'
STATIC_ROOT = rel_path('/static')

#Admin
LOGIN_URL = '/admin/'
ADMIN_MEDIA_PREFIX = STATIC_URL + "grappelli/"
ADMINS = (
    ('Saul Shanabrook', 's.shanabrook@gmail.com'),
  )


#Urls
ROOT_URLCONF = 'letters.urls'

#Templates
TEMPLATE_DIRS = (
    rel_path('templates'),
  )

MIDDLEWARE_CLASSES = add_to_middleware(
    MIDDLEWARE_CLASSES,
    'django.middleware.gzip.GZipMiddleware',
    prepend=True)

#Users
AUTH_PROFILE_MODULE = 'letters.UserProfile'

#Database
DATABASES = {
    'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME':  rel_path('sqlite.db'),
            'USER': '',
            'PASSWORD': '',
            'HOST': '',
            'PORT': '',
            }
    }

########
#Cache
########

MIDDLEWARE_CLASSES = add_to_middleware(
    MIDDLEWARE_CLASSES,
    'django.middleware.cache.UpdateCacheMiddleware',
    prepend=True)
MIDDLEWARE_CLASSES = add_to_middleware(
    MIDDLEWARE_CLASSES,
    'django.middleware.cache.FetchFromCacheMiddleware')

CACHE_MIDDLEWARE_KEY_PREFIX = ''
CACHE_MIDDLEWARE_SECONDS = 600

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}

########
#Security
########
#SECURE_FRAME_DENY = True
#SECURE_HSTS_SECONDS = 1
#SESSION_COOKIE_HTTPONLY = True
#USE_I18N = False
SECRET_KEY = 'n39qmq9^(!ab6p31t3ex8zj0q!gp12c&-r_+nrlb#j^v+=!(-r'
INTERNAL_IPS = '127.0.0.1,23, 21.179.154, 174.129.17.131'

TEMPLATE_CONTEXT_PROCESSORS += ('django.core.context_processors.csrf',)
