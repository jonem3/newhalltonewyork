from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
from .retrieve_club import retrieve_club
from .retrieve_data import retrieve
import datetime
from highcharts.views import (HighChartsMultiAxesView, HighChartsPieView,
                              HighChartsSpeedometerView, HighChartsHeatMapView, HighChartsPolarView)

def index(request):
    data = retrieve_club()
    #data = data.replace("[]", "")
    #data=json.loads(data)
    distance_total = 0
    moving_total =0
    """
        for i in data:
        distance_total += i['distance']
        moving_total += i['moving_time']
    distance_total = distance_total/1000
    distance_total = round(distance_total, 2)
    timeelapsed = str(datetime.timedelta(seconds=moving_total))[:-3]
    """

    return HttpResponse(data)
# Create your views here.






