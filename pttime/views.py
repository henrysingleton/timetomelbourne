from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('Im an index, hello!')


def bulkcreate(request):
    return render(request, 'pttime/bulkcreate.html')