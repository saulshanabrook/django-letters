from letters.settings.base import *

########
#Database
########
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
