from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=300, null=True, blank=True)

    class Meta:
        ordering = ["id"]


class Measurement(models.Model):
    temperature = models.DecimalField(max_digits=4, decimal_places=1, default=True)
    created_at = models.DateTimeField(auto_now=True)
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')

    class Meta:
        ordering = ["-created_at"]

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)
