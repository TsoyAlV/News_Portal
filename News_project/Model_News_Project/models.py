from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    rating = models.IntegerField(default=0)
    user_key = models.ForeignKey(User, on_delete=models.CASCADE)

#Тут может быть недопонимание понятия самого метода
    def update_rating(self):
        pass
        #self.k = self.rating
        #self.k += self.user_key.
        #return self.rating


class Category(models.Model):
    category = models.CharField(max_length=50, unique=True)


YEAR_IN_SCHOOL_CHOICES = [
    ('ar', 'Article'),
    ('nw', 'News')
]


class Post(models.Model):
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    time_creating = models.DateTimeField(auto_now_add=True)

    News = 'nw'
    Article = 'ar'
    ar_nw = [
        (Article, 'Article'),
        (News, 'News')
    ]
    choice_ar_nw = models.CharField(
        max_length=2,
        choices=ar_nw,
        default=Article,
    )

    category = models.ManyToManyField(Category, through='PostCategory')
    tittle = models.CharField(max_length=50)
    content = models.TextField()
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1

    def dislike(self):
        self.rating -= 1

    def preview(self):
        return f'{self.content[:5]}...' # Здесь может быть ошибка!!!



class PostCategory(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    context = models.TextField()
    datetime_comment = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1

    def dislike(self):
        self.rating -= 1





