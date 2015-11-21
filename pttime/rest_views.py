from nap.rest import views

from . import mappers
from . import models


class LocationListView(views.ListPostMixin, views.ListGetMixin, views.BaseListView):
    model = models.Location
    mapper_class = mappers.LocationMapper
