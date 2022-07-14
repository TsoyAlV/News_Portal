from django.forms import ModelForm, CharField, EmailField, IntegerField, BooleanField
from .models import News

class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = ['name', 'category', 'content',]
