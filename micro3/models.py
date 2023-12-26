from django.db import models


class CalculateData(models.Model):
    layer = models.CharField(max_length=50)
    element = models.CharField(max_length=50)
    kpi = models.FloatField()

    def __str__(self):
        return f'{self.layer}, {self.element}, {self.kpi}'


