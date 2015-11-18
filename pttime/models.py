from django.db import models
from djgeojson.fields import PointField


# Create your models here.
class Location(models.Model):
    postcode = models.IntegerField()
    suburb = models.CharField(max_length=200)
    landmark = models.CharField(max_length=200, blank=True)
    geolocation = PointField()
