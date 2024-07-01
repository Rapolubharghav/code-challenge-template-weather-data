from django.db import models


class WeatherRecord(models.Model):
    """ Weather record model representing individual weather data entries """
    station_id = models.CharField(max_length=255, null=False)
    date = models.DateField(null=False)
    max_temp = models.FloatField(null=True)
    min_temp = models.FloatField(null=True)
    precipitation = models.FloatField(null=True)

    class Meta:
        db_table = 'weather_records'


class WeatherStats(models.Model):
    """ Weather statistics model aggregating data for each station and year """
    station_id = models.CharField(max_length=255, null=False)
    year = models.IntegerField(null=False)
    avg_max_temp = models.FloatField(null=True)
    avg_min_temp = models.FloatField(null=True)
    total_precipitation = models.FloatField(null=True)

    class Meta:
        db_table = 'weather_stats'