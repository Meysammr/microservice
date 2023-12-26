from django.db.models import Sum, Max, Min, Avg

FUNCTION_MAPPING = {
    "SUM": Sum,
    "AVG": Avg,
    "MIN": Min,
    "MAX": Max,
}