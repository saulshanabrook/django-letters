from django.conf.global_settings import *
import datetime

from letters.functions import rel_path, add_to_middleware

########
#Packages
########
INSTALLED_APPS += (
    'letters.comments',
    'letters.posts',
    'letters.users',

    'south',
  )


########
#Django
########
SITE_ID = 1


INSTALLED_APPS += (
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

#Urls
ROOT_URLCONF = 'letters.urls'

#Templates
TEMPLATE_DIRS = (
    rel_path('templates'),
  )

#Users
AUTH_PROFILE_MODULE = 'letters.users.UserProfile'
