from django.db import models
from micro1.models import Raw


class Aggregations(models.Model):
    kpi = models.CharField(max_length=50)
    value = models.FloatField()

    #relations
    raw_data = models.ForeignKey(Raw, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.raw_data.city}, {self.raw_data.province}, {self.kpi}'


