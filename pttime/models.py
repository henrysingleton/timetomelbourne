from django.db import models
from djgeojson.fields import PointField

# Create your models here.
class Location(models.Model):
    postcode = models.IntegerField(max_length=4)
    suburb = models.CharField(max_length=200)
    landmark = models.CharField(max_length=200)
    geolocation = PointField()