import django_filters

from .models import Pdx


class PdxFilter(django_filters.FilterSet):
    """
    Defines Pdx model fields that can be used to filter results.
    """

    class Meta:
        model = Pdx
        fields = ['diagnosis', 'tumor_type', 'primary_site', 'collection_site',
                  'engraftment_site', 'engraftment_type']
