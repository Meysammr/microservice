import uuid
from django.db import models


class Raw(models.Model):
    
    raw_id = models.UUIDField(default=uuid.uuid4, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    province = models.CharField(max_length=200, null=True, blank=True)
    day = models.DateTimeField(null=True, blank=True)
    kpi_1 = models.FloatField(null=True, blank=True)
    kpi_2 = models.FloatField(null=True, blank=True)
    kpi_3 = models.FloatField(null=True, blank=True)
    kpi_4 = models.FloatField(null=True, blank=True)
    kpi_5 = models.FloatField(null=True, blank=True)
    kpi_6 = models.FloatField(null=True, blank=True)
    kpi_7 = models.FloatField(null=True, blank=True)
    kpi_8 = models.FloatField(null=True, blank=True)
    kpi_9 = models.FloatField(null=True, blank=True)
    kpi_10 = models.FloatField(null=True, blank=True)
    kpi_11= models.FloatField(null=True, blank=True)
    kpi_12 = models.FloatField(null=True, blank=True)
    kpi_13 = models.FloatField(null=True, blank=True)
    kpi_14 = models.FloatField(null=True, blank=True)
    kpi_15 = models.FloatField(null=True, blank=True)
    kpi_16 = models.FloatField(null=True, blank=True)
    kpi_17 = models.FloatField(null=True, blank=True)
    kpi_18 = models.FloatField(null=True, blank=True)
    kpi_19 = models.FloatField(null=True, blank=True)
    kpi_20 = models.FloatField(null=True, blank=True)


