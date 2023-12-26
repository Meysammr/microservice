from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.db.models import Sum, Max, Min, Avg

from micro1.models import Raw

from .serializers import AggregationResultSerializer
from .Aggregations import FUNCTION_MAPPING


class AggregationView(APIView):
    def get(self, request, *args, **kwargs):

        aggregations_config = {
                "kpi_1": 'SUM',
                "kpi_2": 'AVG',
                "kpi_3": 'MIN',
                "kpi_4": 'MAX',
                "kpi_5": 'MIN',
                "kpi_6": 'AVG',
                "kpi_8": 'MAX',
                "kpi_9": 'MAX',
                "kpi_10": 'SUM',
                "kpi_11": 'SUM',
                "kpi_12": 'MIN',
                "kpi_13": 'AVG',
                "kpi_14": 'SUM',
                "kpi_15": 'MAX',
                "kpi_16": 'MIN',
                "kpi_17": 'AVG',
                "kpi_18": 'MAX',
                "kpi_19": 'SUM',
                "kpi_20": 'MAX',
            }

        aggregation_results = []

        for kpi, function_name in aggregations_config.items():
            aggregation_function = FUNCTION_MAPPING.get(function_name, None)
            if aggregation_function:
                result = Raw.objects.filter(city__isnull=False, province__isnull=False).values('city',
                                                                                        'province').annotate(
                result=aggregation_function(f'{kpi}'))
                results = list(result)
                aggregation_results.extend([{'city': result['city'], 'province': result['province'], 'kpi': kpi, 'result': result['result']} for result in results])
                serializer = AggregationResultSerializer(aggregation_results, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
