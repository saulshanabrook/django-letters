import os


if os.getenv('production_setting') == 'Heroku':
    from letters.settings.remote import *
else:
    from letters.settings.local import *

TEMPLATE_DEBUG = DEBUG