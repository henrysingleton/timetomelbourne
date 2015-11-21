from nap.rest import views
import json

from . import mappers
from . import models
from .models import Location
from django.http import HttpResponse



class LocationListView(views.ListPostMixin, views.ListGetMixin, views.BaseListView):
    model = models.Location
    mapper_class = mappers.LocationMapper


def post_bulk_create(request):
    json_str = request.body.decode(encoding='UTF-8')
    json_obj = json.loads(json_str)

    location_objects = [
        Location(
            suburb=location['suburb'],
            postcode=location['postcode'],
        )
        for location in json_obj['data']
    ]

    msg = models.Location.objects.bulk_create(location_objects)

    return HttpResponse(msg)
