from django.urls import path
from django.views.decorators.cache import cache_page

from . import views
from .chart_build import chart_json, distances_json, distance_json
from .view import line_chart, line_chart_json, LineChartJSONView, map_view, videos_view, main

urlpatterns = [
    path('', main, name='main'),
    path('charts/', line_chart, name='line_chart'),
    path('chart.json', chart_json, name='line_chart_json'),
    path('distances.json', distances_json, name='distances_chart_json'),
    path('distance.json', distance_json, name='distance_chart_json'),
    path('map/', map_view, name='map'),
    path('videos/', videos_view, name='videos')
    #path('chart.json', cache_page(500)(LineChartJSONView.as_view()), name='line_chart_json'),
]
