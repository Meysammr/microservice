from rest_framework import serializers
from .models import Raw


class RawSerializer(serializers.ModelSerializer):
    class Meta:
        model = Raw
        fields = '__all__'