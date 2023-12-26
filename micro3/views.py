# mymicroservice/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from micro1.models import Raw
from micro2.models import Aggregations

from .models import CalculateData
from .serializers import CalculateDataSerializer, OutputSerializer


class FormulaCalculation(APIView):

    def post(self, request, *args, **kwargs):
        serializer = CalculateDataSerializer(data=request.data)
        if serializer.is_valid():
            layer = serializer.validated_data['layer']
            print(layer)
            elements = serializer.validated_data.get('elements', '')
            print(elements)
            kpi = serializer.validated_data['kpi']
            print(kpi)

            if Aggregations.objects.filter(raw_data__city=elements, raw_data__province=layer, kpi=kpi).exists():
                data_from_db = Aggregations.objects.filter(raw_data__city__in=elements, raw_data__province=layer,
                                                           kpi=kpi)

                formula_data_list = []
                for entry in data_from_db:
                    element = f"{entry.raw_data.city} - {entry.raw_data.province}"
                    kpi_value = entry.value
                    formula_data = CalculateData(layer=layer, element=element, kpi_value=kpi_value)
                    formula_data_list.append(formula_data)

                output_data = {'result': formula_data_list}
                output_serializer = OutputSerializer(output_data, many=True)
                return Response(output_serializer.data, status=status.HTTP_200_OK)

        return Response({'message': 'something wrong'}, status=status.HTTP_400_BAD_REQUEST)
