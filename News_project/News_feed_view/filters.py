from django_filters import FilterSet, DateFilter
from .models import News

class NewsFilter(FilterSet):
    # Здесь в метах классе надо предоставить модель и указать поля, по которым будет фильтроваться

    class Meta:
        model = News
        fields = {
            'name': ['icontains'],
            'content': ['icontains'],
            'category': ['exact'],
            'datetime_pub': ['lte'],
            }
