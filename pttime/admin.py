from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from .models import Location, Route
import json


class LocationAdmin(LeafletGeoAdmin):
    list_display = (['coordinates','suburb','postcode','landmark'])
    fields = ['postcode', 'suburb', 'landmark', 'geolocation', 'raw_geo_data']
    readonly_fields = ['raw_geo_data']

    def raw_geo_data(self, obj):
        return obj.geolocation


admin.site.register(Route)
admin.site.register(Location, LocationAdmin)
