from rest_framework import viewsets

from pdx.models import Pdx
from .permissions import IsAuthorOrReadOnly
from .serializers import PdxSerializer


class PdxViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly, )
    queryset = Pdx.objects.all()
    serializer_class = PdxSerializer
