from .common import *
from ..functions import add_to_middleware

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME':  os.path.join(DIRNAME, '../sqlite.db'),
            'USER': '',
            'PASSWORD': '',
            'HOST': '',
            'PORT': '',
            }
    }

########
# Debug Toolbar
########
MIDDLEWARE_CLASSES = add_to_middleware(
    MIDDLEWARE_CLASSES, 'debug_toolbar.middleware.DebugToolbarMiddleware')
INSTALLED_APPS += (
    'debug_toolbar',
    'django_extensions',
    )
INTERNAL_IPS = ('0.0.0.0', '127.0.0.1',)

########
#Testing
########
TEST_RUNNER = 'discover_runner.DiscoverRunner'
TEST_DISCOVER_TOP_LEVEL = DIRNAME
TEST_DISCOVER_ROOT = os.path.join(DIRNAME, 'tests')

