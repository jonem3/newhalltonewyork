from django.shortcuts import render
from django.http import HttpResponse
import requests
from .retrieve_data import retrieve
import datetime
from highcharts.views import (HighChartsMultiAxesView, HighChartsPieView,
                              HighChartsSpeedometerView, HighChartsHeatMapView, HighChartsPolarView)

def index(request):
    data = retrieve()
    distance_total = 0
    moving_total =0
    for i in data:
        distance_total += i['distance']
        moving_total += i['moving_time']
    distance_total = distance_total/1000
    distance_total = round(distance_total, 2)
    timeelapsed = str(datetime.timedelta(seconds=moving_total))[:-3]
    return HttpResponse("Total distance: {}km, Total Moving Time: {}".format(distance_total, timeelapsed))
# Create your views here.






