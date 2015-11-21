from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt

from . import views
from . import rest_views

urlpatterns = [
    # /
    url(r'^$', views.index, name='index'),

    # /bulk-create (just a view)
    url(r'^bulk-create/$', views.bulkcreate, name='bulkcreate'),

    # Handle the standard REST for Locations (single only)
    url(r'^list/$', csrf_exempt(rest_views.LocationListView.as_view())),

    # Handle the bulk create REST
    url(r'^bulk-list/$', csrf_exempt(rest_views.post_bulk_create)),

]
