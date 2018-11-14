"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

try:
	path = '/home/NelliesNoodles/nelliesnoodles_mysite/mysite'
	if path not in sys.path:
	    sys.path.insert(0, path)

	os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

	application = get_wsgi_application()

except:
	# to update from my computer, home path is different than
        #pythonanywhere path?
	path = '/home/nellie/nelliesnoodles_mysite/mysite'
	if path not in sys.path:
	    sys.path.insert(0, path)

	os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

	application = get_wsgi_application()
