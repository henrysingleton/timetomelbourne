from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from .models import Location, Route
from django.contrib.admin import ModelAdmin


class LocationAdmin(LeafletGeoAdmin):
    list_display = (['coordinates', 'suburb', 'postcode', 'landmark'])
    fields = ['postcode', 'suburb', 'landmark', 'geolocation', 'raw_geo_data']
    readonly_fields = ['raw_geo_data']

    @staticmethod
    def raw_geo_data(obj):
        return obj.geolocation


class RouteAdmin(ModelAdmin):
    list_display = (['origin', 'destination', 'transfers', 'time', 'created', 'updated'])

admin.site.register(Route, RouteAdmin)
admin.site.register(Location, LocationAdmin)
