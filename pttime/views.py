from django.shortcuts import render
from django.http import HttpResponse
from .route_loader import RouteLoader
from . import models


def index(request):
    return HttpResponse('Im an index, hello!')


def bulkcreate(request):
    return render(request, 'pttime/bulkcreate.html')


def load_routes(request):
    destination = models.Location.objects.filter(id=8724)[0]
    routey_loader = route_loader.RouteLoader()
    routey_loader.start(destination=destination, limit=2, start_id=1)
    return HttpResponse('DONE!')


def heatmap(request):
    return render(request, 'pttime/heatmap.html')