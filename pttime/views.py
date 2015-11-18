from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('hahahahahaha')

def bulkcreate(request):
    return render(request, 'pttime/bulkcreate.html')

