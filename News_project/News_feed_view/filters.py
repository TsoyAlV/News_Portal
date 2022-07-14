from django_filters import FilterSet, DateFilter, ChoiceFilter
from django.forms import DateInput
from .models import News


class NewsFilter(FilterSet):
    date_pub = DateFilter(lookup_expr=('lt'), widget=DateInput(attrs={'type': 'date'}))
    class Meta:
        model = News
        fields = {
            'name': ['icontains'],
            'category': ['exact']
        }

class NewsSimpleFilter(FilterSet):
    class Meta:
        model = News
        fields = {
            'name': ['icontains']
        }
