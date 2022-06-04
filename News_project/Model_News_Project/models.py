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

#для нахождения рейтинга всех комментариев пользователя с user_id ==
def rating_comments_of_user(user_id_inlet):
    list_comment_of_user = list(Comment.objects.filter(user_id = user_id_inlet))
    rating = 0
    for _ in range(len(list_comment_of_user)):
        rating += list_comment_of_user[_].rating
    return rating

#для нахождения рейтинга постов пользователя
def rating_posts_of_user(user_id):
    list_post_of_user = list(Post.objects.filter(author_id = user_id))
    rating = 0
    for _ in range(len(list_post_of_user)):
        rating += list_post_of_user[_].rating
    return rating*3

#для нахождения рейтинга комментарий пользователя
def rating_comments_of_post_of_user(user_id):
    list_post_of_user = list(Post.objects.filter(author_id = user_id))
    rating = 0
    for _ in range(len(list_post_of_user)):
        list_comment_of_post_of_user = list(Comment.objects.filter(post_id = list_post_of_user[_]))
        for _i in range(len(list_comment_of_post_of_user)):
            if list_comment_of_post_of_user[_i].user_id == user_id:
                pass
            else:
                rating += list_comment_of_post_of_user[_i].rating
    return rating


class Author(models.Model):
    rating = models.IntegerField(default=0)
    #user_key = models.ForeignKey(User, on_delete=models.CASCADE)
    #fk = User.objects.get(username=user_key).id
    def update_rating(fk):
        rating = rating_posts_of_user(fk) + rating_comments_of_post_of_user(fk) + rating_comments_of_user(fk)
        return rating

