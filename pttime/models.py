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
        if self.geolocation and self.geolocation['coordinates'][0] and self.geolocation['coordinates'][1]:
            return '%s,%s' % (self.geolocation['coordinates'][0], self.geolocation['coordinates'][1])
        else:
            return ''

    coordinates = property(_get_coordinates)

    def save(self, *args, **kwargs):
        if self.geolocation and self.geolocation['coordinates'][0] and self.geolocation['coordinates'][1] and self.geolocation['coordinates'][1] < 0:
            self.geolocation['coordinates'] = {self.geolocation['coordinates'][1], self.geolocation['coordinates'][0]}

        super(Route, self).save(*args, **kwargs)  # Call the "real" save() method.


class Route(models.Model):
    origin = models.ForeignKey(Location, related_name='origin')
    destination = models.ForeignKey(Location, related_name='destination')
    transfers = models.IntegerField(null=True)
    time = models.DurationField(null=True)
    walking_time = models.DurationField(null=True)
    pain = models.IntegerField(null=True)
    score = models.IntegerField(null=True)
    response = models.TextField(null=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    possible = models.BooleanField(default=True)

    def calculate_score(self):
        # We want to calculate a score. Maybe dont worry about this yet, and just do times?
        self.score = 1

    def calculate_pain(self):
        self.pain = 1

    def save(self, *args, **kwargs):
        self.calculate_pain()
        self.calculate_score()
        super(Route, self).save(*args, **kwargs)  # Call the "real" save() method.
