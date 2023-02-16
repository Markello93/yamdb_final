from django_filters import rest_framework as filters

from reviews.models import Title


class FilterForTitle(filters.FilterSet):
    genre = filters.CharFilter(
        field_name='genre__slug', lookup_expr='icontains'
    )
    category = filters.CharFilter(
        field_name='category__slug', lookup_expr='icontains'
    )
    year = filters.NumberFilter(field_name='year', lookup_expr='contains')
    name = filters.CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        fields = ['name', 'year', 'genre', 'category']
        model = Title
