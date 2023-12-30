# micro3/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import F, ExpressionWrapper, fields
from .serializers import InputSerializer, RawSerializer
from micro1.models import Raw


class FormulaCalculation(APIView):

    def post(self, request, *args, **kwargs):
        serializer = InputSerializer(data=request.data)
        if serializer.is_valid():
            layer = serializer.validated_data['layer']
            elements = serializer.validated_data.get('elements', [])
            kpi_formula = serializer.validated_data['kpi']

            # Prepare dictionary for kpi variables
            kpi_variables = {f'kpi_{i}': F(f'kpi_{i}') for i in range(1, 21)}

            # Evaluate the formula with variables
            try:
                result_formula = eval(kpi_formula, {}, kpi_variables)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

            # Filter Raw objects based on layer and elements
            if layer == 'site':
                data = Raw.objects.filter(province__in=elements)
            elif layer == 'city':
                data = Raw.objects.filter(city__in=elements)

            # Annotate the result of the formula
            data = data.annotate(result=ExpressionWrapper(result_formula, output_field=fields.FloatField()))

            # Serialize the results and return the response
            result_serializer = RawSerializer(data, many=True)
            return Response(result_serializer.data, status=status.HTTP_200_OK)

        return Response({'message': 'Invalid input'}, status=status.HTTP_400_BAD_REQUEST)
