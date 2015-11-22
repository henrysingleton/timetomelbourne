from .models import Location, Route


class RouteLoader:
    def locations_requiring_update(self):
        """Find all locations that will need an update and return them. IE those that have no routes against them,
        or that only have routes against them that are stale"""

        return Location.objects.all()

    def start(self, start_id, limit):
        locations = self.locations_requiring_update()

        for location in locations:
            route_data = self.fetch_route_data()
            Route.xml_response = route_data
            # do more saving of fields here. 

    def fetch_route_data(self):
        return 'do the bing api request here'
