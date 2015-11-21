from django.contrib.auth.models import User
from nap import datamapper
from . import models


class UserMapper(datamapper.ModelDataMapper):
    class Meta:
        model = User
        fields = '__all__'


class LocationMapper(datamapper.ModelDataMapper):
    class Meta:
        model = models.Location
        fields = '__all__'
