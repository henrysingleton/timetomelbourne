import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core.cache import cache
from .route_loader import RouteLoader
from . import models
from . import tasks
from django.views.generic import ListView


def index(request):
    return HttpResponse('Im an index, hello!')


def bulkcreate(request):
    return render(request, 'pttime/bulkcreate.html')


# This is using outdated version of routey loader. Don't use this since route loading should be triggered by
# the queue runner
def load_routes(request):
    destination = models.Location.objects.filter(id=8724)[0]
    routey_loader = RouteLoader()
    routey_loader.start(destination=destination, limit=2, start_id=1)
    return HttpResponse('DONE!')


# Heatmap page is pretty basic currently because it loads content via JS.
def heatmap(request):
    return render(request, 'pttime/heatmap.html')


# This is the json response to get all the points.
def address_points(request):
    if cache.get('heatmapData') is None:
        data = models.Route.objects.filter(possible=True)
        points = []
        for point in data:
            points.append([point.origin.geolocation['coordinates'][0],
                           point.origin.geolocation['coordinates'][1],
                           point.time.total_seconds()/100])

        cache.set('heatmapData', points, 300)
    return JsonResponse(cache.get('heatmapData'), safe=False)
