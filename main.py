import os, sys
print(sys.path)
os.environ['DJANGO_SETTINGS_MODULE'] = 'project_name.settings'
import django
django.setup()
from django.contrib.auth.models import User

