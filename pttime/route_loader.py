from .models import Location
from . import bingmaps


class RouteLoader:


    def locations_requiring_update(self):
        """Find all locations that will need an update and return them. IE those that have no routes against them,
        or that only have routes against them that are stale"""

        return Location.objects.all()

    def start(self, start_id, destination, limit):
        locations = self.locations_requiring_update()


        for location in locations:
            waypoints = [location.coordinates, destination.coordinates]
            results = bingthing.get_routes(waypoints, travel_mode='Transit', date_time='9:00:00AM', time_type='Arrival')
