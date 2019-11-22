import os
import sys


path = '/var/www/zastr'
if path not in sys.path:
    sys.path.insert(0, path)

sys.path.append("/var/www/zastr/myvenv/lib/python3.5/site-packages")
os.environ['DJANGO_SETTINGS_MODULE'] = 'zastroishik.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
