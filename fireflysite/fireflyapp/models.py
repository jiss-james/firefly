from django.db import models

# Create your models here.// What else do we need here ?
class DarkSky(models.Model):
    long = models.CharField(max_length=30)
    lat = models.CharField(max_length=30)
    temperature = models.CharField(max_length=30)
    humidity = models.CharField(max_length=30)
    timestamp = models.CharField(max_length=30)
    windBearing = models.CharField(max_length=30)
    windGust = models.CharField(max_length=30)
    windSpeed = models.CharField(max_length=30)