import django_filters
from .models import Article, Tag, Comment
from django.contrib.auth.models import User

class ArticleFilter(django_filters.FilterSet):
    year = django_filters.NumberFilter(field_name='publication_date', lookup_expr='year')

    month = django_filters.NumberFilter(field_name='publication_date', lookup_expr='month')

    authors = django_filters.ModelMultipleChoiceFilter(
        field_name='authors',
        queryset=User.objects.all()
    )

    tags = django_filters.ModelMultipleChoiceFilter(
        field_name='tags',
        queryset=Tag.objects.all()
    )

    keywords = django_filters.CharFilter(method='filter_by_keyword', label='Keyword Search')

    class Meta:
        model = Article
        fields = ['year', 'month', 'authors', 'tags', 'keywords']

    def filter_by_keyword(self, queryset, name, value): # Custom filter method
        return queryset.filter(title__icontains=value) | queryset.filter(abstract__icontains=value)