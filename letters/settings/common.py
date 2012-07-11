import os

from django.conf.global_settings import *

from ..functions import add_to_middleware

DIRNAME = os.path.join(os.path.dirname(__file__), '../')

########
#Letters
########
INSTALLED_APPS = (
    'letters.apps.comments',
    'letters.apps.posts',
    'letters.apps.users',

  )


########
#External Packages
########
INSTALLED_APPS += (
    'south',
  )


########
#Django
########
DEBUG = False

INSTALLED_APPS += (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.staticfiles',
    'django.contrib.markup',
  )

#Static/Media
STATICFILES_DIRS = (
    ('letters', os.path.join(DIRNAME, 'static')),
  )

MEDIA_URL = '/media/'

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(DIRNAME, '../static/')
MEDAIA_ROOT = os.path.join(DIRNAME, '../media')


#Urls
ROOT_URLCONF = 'letters.urls'

#Templates
TEMPLATE_DIRS = (
    os.path.join(DIRNAME, 'templates'),
  )

MIDDLEWARE_CLASSES = add_to_middleware(MIDDLEWARE_CLASSES,
                                       'django.middleware.gzip.GZipMiddleware',
                                       prepend=True)
DATE_FORMAT = 'F j, Y'

#

########
#Security
########
SECURE_FRAME_DENY = True
SECRET_KEY = '*itk&52%kmo)f0+ase$uvsy6cmz04c@xr#7$n+bn7_=3wv0lz4'

TEMPLATE_CONTEXT_PROCESSORS += ('django.core.context_processors.csrf',)
