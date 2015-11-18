from django.conf.urls import url

from . import views

urlpatterns = [
    #/
    url(r'^$', views.index, name='index'),
    #/bulk-create
    url(r'^bulk-create/$', views.bulkcreate, name='bulkcreate'),

]
