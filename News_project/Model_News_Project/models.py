from django.db import models
from django.contrib.auth.models import User

class Author:

    rank = models.IntegerField(default=0)
    User = User.objects.create_user('my_user_name', 'my_email', 'my_password')
