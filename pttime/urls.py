from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt

from . import views
from . import rest_views

urlpatterns = [
    # /
    url(r'^$', views.index, name='index'),

    # /bulk-create (just a view)
    url(r'^bulk-create/$', views.bulkcreate, name='bulkcreate'),

    # Handle the bulk create REST
    url(r'^bulk-list/$', csrf_exempt(rest_views.post_bulk_create)),

    # Some resty-rest for your fancy furniture! (Just some standard list bits)
    url(r'^points/list/$', csrf_exempt(rest_views.LocationListView.as_view())),

    # Mainly for the delete endpoint
    url(r'^points/view/(?P<pk>\d+)/$', csrf_exempt(rest_views.LocationDetailView.as_view())),

    # Some resty-rest for your fancy furniture! (Just some standard list bits)
    url(r'^load-routes/$', views.load_routes),

    # View the actual heatmap
    url(r'^heatmap/$', views.heatmap),

    # Address Points (JSON output)
    url(r'^address_points/$', views.address_points),

]
