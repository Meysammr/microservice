from django.http import HttpResponse
from .utils import calculate_aggregations


def create_aggregations(request):
    created_aggregations = calculate_aggregations()

    if created_aggregations is not None:
        for aggregation in created_aggregations:
            print(f"Aggregation: {aggregation}")

        return HttpResponse('Aggregations created successfully!')
    else:
        return HttpResponse('Error in creating aggregations!')
