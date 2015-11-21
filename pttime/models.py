from django.db import models
from djgeojson.fields import PointField
# import json


# Create your models here.
class Location(models.Model):
    postcode = models.CharField(blank=True, max_length=5)
    suburb = models.CharField(max_length=200, blank=True)
    landmark = models.CharField(max_length=200, blank=True)
    geolocation = PointField(blank=True)

    # def do_bulk_create(points):
    #
    #     # convert json to objects or something
    #
    #
    #     points = json.loads(points)
    #
    #     location_objs = [
    #         Location(
    #             location = point.whatever
    #         )
    #         for point in points
    #     ]
    #     msg = Location.objects.bulk_create(location_objs)
