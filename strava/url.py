from django.urls import path
from django.views.decorators.cache import cache_page

from . import views
from .chart_build import chart_json, distances_json
from .view import line_chart, line_chart_json, LineChartJSONView

urlpatterns = [
    path('', line_chart, name='line_chart'),
    path('chart.json', chart_json, name='line_chart_json'),
    path('distances.json', distances_json, name='distances_chart_json')
    #path('chart.json', cache_page(500)(LineChartJSONView.as_view()), name='line_chart_json'),
]
