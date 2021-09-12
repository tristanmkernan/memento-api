import django_filters

from .models import MementoCategory

class MementoCategoryFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    category_id = django_filters.CharFilter(lookup_expr="exact")

    class Meta:
        model = MementoCategory
        fields = ("name", "category_id")
