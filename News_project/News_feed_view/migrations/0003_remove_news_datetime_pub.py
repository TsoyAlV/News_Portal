# Generated by Django 4.0.5 on 2022-07-24 23:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('News_feed_view', '0002_news_datetime_pub'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='datetime_pub',
        ),
    ]
