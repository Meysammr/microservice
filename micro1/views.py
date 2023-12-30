
import csv
from contextlib import contextmanager
from django.db import transaction
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Raw
from .serializers import RawSerializer

# Assume you have a serializer for the Raw model named RawSerializer


@contextmanager
def csv_file_reader(file_path):
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        yield reader


class RawDataAPIView(APIView):
    def post(self, request):
        file_path = "/home/meysammr/Downloads/data.csv"
        with self.read_and_bulk_create(file_path):
            return Response({"message": "Data imported successfully"}, status=status.HTTP_201_CREATED)

    @staticmethod
    @contextmanager
    def read_and_bulk_create(file_path):
        with csv_file_reader(file_path) as reader:
            data_to_create = []
            for row in reader:
                # Customize the mapping based on your CSV structure
                serialized_data = RawSerializer(data={
                    "city": row["city"],
                    "province": row["province"],
                    "day": row["day"],
                    "kpi_1": row["kpi_1"],
                    "kpi_2": row["kpi_2"],
                    "kpi_3": row["kpi_3"],
                    "kpi_4": row["kpi_4"],
                    "kpi_5": row["kpi_5"],
                    "kpi_6": row["kpi_6"],
                    "kpi_7": row["kpi_7"],
                    "kpi_8": row["kpi_8"],
                    "kpi_9": row["kpi_9"],
                    "kpi_10": row["kpi_10"],
                    "kpi_11": row["kpi_11"],
                    "kpi_12": row["kpi_12"],
                    "kpi_13": row["kpi_13"],
                    "kpi_14": row["kpi_14"],
                    "kpi_15": row["kpi_15"],
                    "kpi_16": row["kpi_16"],
                    "kpi_17": row["kpi_17"],
                    "kpi_18": row["kpi_18"],
                    "kpi_19": row["kpi_19"],
                    "kpi_20": row["kpi_20"],
                })
                if serialized_data.is_valid():
                    data_to_create.append(serialized_data.validated_data)
                else:
                    return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)

            with transaction.atomic():
                Raw.objects.bulk_create([Raw(**data) for data in data_to_create])
            yield

