from rest_framework import serializers
from pdx.models import Pdx


class PdxSerializer(serializers.ModelSerializer):
    """
    Serializes data from the Pdx class in models.py
    """

    class Meta:
        model = Pdx
        fields = '__all__'
