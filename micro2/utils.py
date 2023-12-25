from django.db.models import Sum, Avg, Min, Max
from .models import Aggregations

from micro1.models import Raw


FUNCTION_MAPPING = {
    "SUM": Sum,
    "AVG": Avg,
    "MIN": Min,
    "MAX": Max,
}


def calculate_aggregations():
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

    for kpi, aggregation_function in aggregations_config.items():
        data = Raw.objects.values("city", "province").annotate(value=FUNCTION_MAPPING[aggregation_function](f'{kpi}'))

        for entry in data:
            raw_data_instances = Raw.objects.filter(city=entry['city'], province=entry['province'])
            if raw_data_instances.exists():
                raw_data_instance = raw_data_instances.first()
                Aggregations.objects.create(
                    raw_data=raw_data_instance,
                    kpi=kpi,
                    value=entry['value']
                )