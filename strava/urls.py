from django.urls import path
from . import views
from .view import line_chart, line_chart_json

urlpatterns = [
    path('', views.index, name='index'),
]
