from rest_framework import serializers


class MathOperationField(serializers.Field):
    def to_internal_value(self, data):
        try:
            eval(data)
        except Exception as e:
            raise serializers.ValidationError(f"Invalid math operation: {e}")

        return data


class CalculateDataSerializer(serializers.Serializer):
    layer = serializers.ChoiceField(choices=['city', 'province'])
    # elements = serializers.ListField()
    elements = serializers.ListField(child=serializers.CharField())
    kpi = serializers.CharField()


class OutputSerializer(serializers.Serializer):
    result = CalculateDataSerializer(many=True)