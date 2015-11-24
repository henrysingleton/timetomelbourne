from .models import Location, Route
from . import bingmaps

class RouteLoader:

    provider = 'bing'

    def locations_requiring_update(self):
        """Find all locations that will need an update and return them. IE those that have no routes against them,
        or that only have routes against them that are stale"""

        return Location.objects.all()

    def start(self, start_id, limit):
        locations = self.locations_requiring_update()

        for location in locations:

            params = []

            response = bingmaps.make_request('Routes/Transit', params)


            Route.xml_response = route_data
            # do more saving of fields here.