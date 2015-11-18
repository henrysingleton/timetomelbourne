from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from .models import Location

admin.site.register(Location, LeafletGeoAdmin)
