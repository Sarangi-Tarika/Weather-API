from django.db import models

# Create your models here.
class Weather(models.Model):
    date = models.CharField(max_length=20)
    max_temp = models.IntegerField()
    min_temp = models.IntegerField()
    precipitation = models.IntegerField()
    station_name = models.CharField(max_length=20)

    class Meta:
        unique_together = ("date", "station_name")

class Stats(models.Model):
    date = models.CharField(max_length=20)
    station_name = models.CharField(max_length=20)
    avg_max_temp = models.IntegerField()
    avg_min_temp = models.IntegerField()
    total_acc_ppt = models.IntegerField()

    class Meta:
        unique_together = ("date", "station_name")