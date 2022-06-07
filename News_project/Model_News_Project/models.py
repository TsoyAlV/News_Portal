from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    category = models.CharField(max_length=50, unique=True)


choiced_post = [
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
        choices=choiced_post,
        default=Article,
    )

    category = models.ManyToManyField(Category, through='PostCategory')
    tittle = models.CharField(max_length=50)
    content = models.TextField()
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        prev_text = 126 if len(self.content)>126 else len(self.content)
        return self.content[:prev_text]+'...'


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
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()


class Author(models.Model):
    rating = models.IntegerField(default=0)
    user_key = models.ForeignKey(User, on_delete=models.CASCADE)
    #
    def update_rating(self):
        self.rating_post = self.post_set.filter(author = self).aggregate(total_rating = models.Sum('rating'))['total_rating']*3
        self.rating_comments_of_author = self.user_key.comment_set.exclude(post__in = self.post_set.filter(author = self)).\
            filter(user = self.user_key).aggregate(total_rating=models.Sum('rating'))['total_rating']
        self.rating_comments_of_users = Post.objects.filter(author = self).aggregate(total_rating=models.Sum('rating'))['total_rating']
        self.rating = self.rating_post + self.rating_comments_of_users + self.rating_comments_of_author
        self.save()

