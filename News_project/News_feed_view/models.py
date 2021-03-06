from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User

class News(models.Model):
    name = models.CharField(
        max_length=124,
        unique=True
    )
    content = models.TextField()
    category = models.ForeignKey(
        to = 'Category',
        on_delete=models.CASCADE,
        related_name='news'
    )
    datetime_pub = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.name.title()}: {self.content[:20]}...'


class Category(models.Model):
    # названия категорий тоже не должны повторяться
    name = models.CharField(max_length=100, unique=True)


    def __str__(self):
        return self.name.title()
