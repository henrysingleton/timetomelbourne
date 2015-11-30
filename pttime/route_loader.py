from .models import Location, Route
from . import bingmaps


class RouteLoader:

    def locations_requiring_update(self):
        """Find all locations that will need an update and return them. IE those that have no routes against them,
        or that only have routes against them that are stale"""

        results = Location.objects.raw('''SELECT pttime_location.* FROM pttime_location LEFT JOIN pttime_route ON pttime_route.origin_id = pttime_location.id WHERE pttime_route.id IS NULL ORDER BY pttime_location.id LIMIT 3''')

        return results

    def start(self, start_id, destination, limit):
        locations = self.locations_requiring_update()

        bingthing = bingmaps.BingMaps(key='Ag3rJe-YpHuknwoKRjZooOoTldyyukufpqLQuyu8VfdXnuqRC7SI30sWMoLtG6bh')



        for location in locations:
            waypoints = [location.coordinates, destination.coordinates]
            print('Processing waypoint %s for id %s' % (waypoints, location.id))
            results = bingthing.get_routes(waypoints, travel_mode='Transit', date_time='9:00:00AM', time_type='Arrival')

            route = Route(origin=location, destination=destination, transfers=0, time='00:00', walking_time='00:00', pain=0, xml_response=results)
            route.save()

            print('Saved route with id %s' % route.id)

