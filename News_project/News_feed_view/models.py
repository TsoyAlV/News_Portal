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
    date_pub = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.name.title()}: {self.content[:20]}...'

    def get_absolute_url(self):  # добавим абсолютный путь, чтобы после создания нас перебрасывало на страницу с товаром
        return f'/news/{self.id}'


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    subscribed_user = models.ManyToManyField(User, through='Subscribers')

    def __str__(self):
        return self.name.title()


class Subscribers(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    cat = models.ForeignKey(to=Category, on_delete=models.CASCADE)




