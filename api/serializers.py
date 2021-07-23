from rest_framework import serializers
from pdx.models import Pdx


class PdxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pdx
        fields = '__all__'
