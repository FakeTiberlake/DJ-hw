from django.urls import path

import stations.views

urlpatterns = [
    path('', stations.views.index, name='index'),
    path('bus_stations/', stations.views.bus_stations, name='bus_stations'),
]