from rest_framework import generics

from pdx.models import Pdx
from .serializers import PdxSerializer


class PdxListView(generics.ListAPIView):
    queryset = Pdx.objects.all()
    serializer_class = PdxSerializer


class PdxDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pdx.objects.all()
    serializer_class = PdxSerializer
