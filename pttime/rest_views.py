from nap.rest import views
from nap.rest.views import (
    ObjectGetMixin, ObjectPutMixin, ObjectPatchMixin, ObjectDeleteMixin,
    BaseObjectView,
)
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
            #suburb=location['suburb'],
            #postcode=location['postcode'],
            geolocation=location['geolocation']
        )
        for location in json_obj['data']
    ]

    msg = models.Location.objects.bulk_create(location_objects)

    return HttpResponse(msg)


class LocationDetailView(ObjectGetMixin,
                         ObjectPutMixin,
                         ObjectPatchMixin,
                         ObjectDeleteMixin,
                         BaseObjectView):
    model = models.Location
    slug_field = 'location_id'
    mapper_class = mappers.LocationMapper
