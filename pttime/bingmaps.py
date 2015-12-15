import requests

from django.conf import settings

BINGMAPS_CONFIG = getattr(settings, 'BINGMAPS', {})


class BingError(Exception):
    pass


class BingRequest(dict):

    def __init__(self, key, url=None, parameters=None):
        self.url = url
        self['key'] = key
        if parameters is not None:
            self.update(parameters)


class BingMaps(object):
    """ API for maps.bing.com
    """

    ROUTES_URL = 'https://dev.virtualearth.net/REST/v1/Routes/Transit'
    ROUTES_FROM_MAJOR_ROADS_URL = 'https://dev.virtualearth.net/REST/v1/Routes/FromMajorRoads'

    def __init__(self, key):
        self.key = key

    def get_routes(self, waypoints, avoid=None, optmz='time', rpo=False, du='km', travel_mode='Driving', date_time=None,
                   time_type=None):
        parameters = dict((("wp.%d" % (i+1), w) for i, w in enumerate(waypoints)))
        parameters.update(dict(optmz=optmz, du=du, travelMode=travel_mode))
        if avoid:
            parameters['avoid'] = avoid

        if rpo:
            parameters['rpo'] = 'Points'

        if date_time:
            parameters['dateTime'] = date_time

        if time_type:
            parameters['timeType'] = time_type

        request = BingRequest(self.key, url=self.ROUTES_URL, parameters=parameters)
        return self.load(request)

    def get_major_routes(self, destination, excl=None, rpo=False, du='km'):
        parameters = dict(dest=destination, du=du)
        if excl:
            parameters['excl'] = excl

        if rpo:
            parameters['rpo'] = 'Points'

        request = BingRequest(self.key, url=self.ROUTES_FROM_MAJOR_ROADS_URL, parameters=parameters)
        return self.load(request)

    def load(self, request):
        try:
            r = requests.get(self.ROUTES_URL, request.items())
            data = r.json()
            assert data['statusCode'] == 200
            return data['resourceSets'][0]['resources'][0]

        # If there was an IO error we want to fail. Currently uncaught.
        except IOError:
            raise BingError("IO Error: Could not load data.")

        # If the data is in a weird form, or we got something other than a 200 status, return it.
        except (AssertionError, KeyError, IndexError):
            return data
