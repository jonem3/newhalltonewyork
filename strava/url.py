from django.urls import path
from . import views
from .view import line_chart, line_chart_json

urlpatterns = [
    path('', line_chart, name='line_chart'),
    path('chart.json', line_chart_json, name='line_chart_json'),
]
