from rest_framework import generics
from pdx.models import Pdx
from .serializers import PdxSerializer


class PdxAPIView(generics.ListAPIView):
    queryset = Pdx.objects.all()
    serializer_class = PdxSerializer
