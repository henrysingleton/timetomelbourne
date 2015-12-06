from .models import Location, Route
from . import bingmaps
from datetime import timedelta
import json
from time import sleep


class RouteLoader:

    def locations_requiring_update(self):
        """Find all locations that will need an update and return them. IE those that have no routes against them,
        or that only have routes against them that are stale"""

        results = Location.objects.raw('''SELECT pttime_location.* FROM pttime_location LEFT JOIN pttime_route ON pttime_route.origin_id = pttime_location.id WHERE pttime_route.id IS NULL ORDER BY pttime_location.id LIMIT 100''')

        return results

    def start(self, start_id, destination, limit):
        locations = self.locations_requiring_update()

        bingthing = bingmaps.BingMaps(key='Ag3rJe-YpHuknwoKRjZooOoTldyyukufpqLQuyu8VfdXnuqRC7SI30sWMoLtG6bh')

        for location in locations:
            waypoints = [location.coordinates, destination.coordinates]
            print('Processing waypoint %s for id %s' % (waypoints, location.id))
            results = bingthing.get_routes(waypoints, travel_mode='Transit', date_time='9:00:00AM', time_type='Arrival')
            parsed_results = self.parse_bing_data(results)

            route = Route(origin=location,
                          destination=destination,
                          transfers=parsed_results['transfers'],
                          time=parsed_results['time'],
                          walking_time=parsed_results['walking_time'],
                          response=json.dumps(results))  # Convert back to JSON for storage.
            route.save()

            print('Saved route with id %s' % route.id)
            sleep(4)

    @staticmethod
    def parse_bing_data(data):
        """

        :param data:
        :return: dict
        """
        ret = dict()
        ret['transfers'] = 0
        ret['time'] = timedelta(seconds=data['travelDuration'])
        ret['walking_time'] = '00:00'

        return ret

        # results['routeLegs'][0]['itineraryItems']  [x]['travelDuration'] ... [x]['iconType'] == Walk
        # OR as XPath sum(/Response/ResourceSets/ResourceSet/Resources/Route/RouteLeg/ItineraryItem[Instruction/@maneuve
        # rType="Walk"]/TravelDuration)
        # <Hint hintType="TimeToMakeConnection"
