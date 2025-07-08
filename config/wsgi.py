import os
import sys

# Add your project directory to the sys.path
path = '/home/alamindrz/mewrite'
if path not in sys.path:
    sys.path.append(path)

# Set the settings module to your actual settings
os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()