import urllib
import json

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

    def to_url(self):
        """ Serialize as a URL for a GET request.
        """
        parameters = urllib.urlencode(self.items())
        return "%s?%s" % (self.url, parameters)


class BingMaps(object):
    """ API for maps.bing.com
    """

    ROUTES_URL = 'https://dev.virtualearth.net/REST/v1/Routes'
    ROUTES_FROM_MAJOR_ROADS_URL = 'https://dev.virtualearth.net/REST/v1/Routes/FromMajorRoads'

    def __init__(self, key):
        self.key = key

    def get_routes(self, waypoints, avoid=None, optmz='time', rpo=False, du='km', travel_mode='Driving'):
        parameters = dict((("wp.%d" % (i+1), w) for i, w in enumerate(waypoints)))
        parameters.update(dict(optmz=optmz, du=du, travelMode=travel_mode))
        if avoid:
            parameters['avoid'] = avoid

        if rpo:
            parameters['rpo'] = 'Points'

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

    @staticmethod
    def load(request):
        try:
            json_data = urllib.urlopen(request.to_url())
            data = json.load(json_data)
            assert data['statusCode'] == 200
            return data['resourceSets'][0]['resources'][0]
        except (IOError, AssertionError):
            raise BingError("Not load data.")
        except (KeyError, IndexError):
            raise BingError("Not parse data.")
