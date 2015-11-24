from django.db import models
from djgeojson.fields import PointField


class Location(models.Model):
    postcode = models.CharField(blank=True, max_length=5)
    suburb = models.CharField(max_length=200, blank=True)
    landmark = models.CharField(max_length=200, blank=True)
    geolocation = PointField(blank=True)

    class Meta:
        verbose_name = "Location Point"

    def _get_coordinates(self):
        if (self.geolocation and self.geolocation['coordinates'][0] and self.geolocation['coordinates'][1]):
            return '%s,%s' % (self.geolocation['coordinates'][0], self.geolocation['coordinates'][1])
        else:
            return ''
    coordinates = property(_get_coordinates)


class Route(models.Model):
    origin = models.ForeignKey(Location, related_name='origin')
    destination = models.ForeignKey(Location, related_name='destination')
    transfers = models.IntegerField()
    time = models.DurationField()
    walking_time = models.DurationField()
    pain = models.IntegerField(null=True)
    xml_response = models.TextField()
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)


