# micro3/serializers.py
from rest_framework import serializers
from micro1.models import Raw


class InputSerializer(serializers.Serializer):
    layer = serializers.ChoiceField(choices=['site', 'city'])
    elements = serializers.ListField(child=serializers.CharField())
    kpi = serializers.CharField()


class RawSerializer(serializers.ModelSerializer):
    class Meta:
        model = Raw
        fields = '__all__'
