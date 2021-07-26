from rest_framework import viewsets

from pdx.models import Pdx
from .serializers import PdxSerializer


class PdxViewSet(viewsets.ModelViewSet):
    queryset = Pdx.objects.all()
    serializer_class = PdxSerializer
