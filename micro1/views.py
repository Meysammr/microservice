from django.shortcuts import render
from django.http import HttpResponse

import csv

from .models import Raw


def import_csv(request):

    # csv_file_path = request.FILES['./data.csv']
    csv_file_path = '/home/meysammr/Downloads/data.csv'

    with open(csv_file_path, 'r') as file:
        reader = csv.DictReader(file)
        data_list = list(reader)

    for data in data_list:
        Raw.objects.create(
            city=data['city'],
            province=data['province'],
            day=data['day'],
            kpi_1=data['kpi_1'],
            kpi_2=data['kpi_2'],
            kpi_3=data['kpi_3'],
            kpi_4=data['kpi_4'],
            kpi_5=data['kpi_5'],
            kpi_6=data['kpi_6'],
            kpi_7=data['kpi_7'],
            kpi_8=data['kpi_8'],
            kpi_9=data['kpi_9'],
            kpi_10=data['kpi_10'],
            kpi_11=data['kpi_11'],
            kpi_12=data['kpi_12'],
            kpi_13=data['kpi_13'],
            kpi_14=data['kpi_14'],
            kpi_15=data['kpi_15'],
            kpi_16=data['kpi_16'],
            kpi_17=data['kpi_17'],
            kpi_18=data['kpi_18'],
            kpi_19=data['kpi_19'],
            kpi_20=data['kpi_20'],
        )
    return HttpResponse('Import success')