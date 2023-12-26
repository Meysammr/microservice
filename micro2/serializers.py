from rest_framework import serializers


class AggregationResultSerializer(serializers.Serializer):
    kpi = serializers.CharField()
    result = serializers.FloatField()
