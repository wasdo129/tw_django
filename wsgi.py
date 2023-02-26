import os
import sys

try:
  sys.path.remove('/usr/lib/python3/dist-packages')
except:
  pass

sys.path.append('/home/c/cu44668/django/public_html/djangotest1/')
sys.path.append('/home/c/cu44668/django/public_html/venv/lib/python3.6/site-packages/')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangotest1.settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

