from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView

from .retrieve_club import retrieve_club
from .retrieve_data import retrieve
import datetime
from .models import Exercises

class LineChartJSONView(BaseLineChartView):
    def get_labels(self):
        names = ["Total Distance/Total Time"]
        return names

    def get_providers(self):

        """Return names of datasets."""
        return ["Total Distance (KM)", "Total Time (Hours)"]

    def get_data(self):
        """Return 3 datasets to plot."""
        totalDistance = 0
        distanceTotal = []
        totalMoving = 0
        movingTotal = []
        start_point =True
        for i in Exercises.objects.filter().order_by("id"):
            totalDistance += round(i.distance/1000, 2)
            totalMoving += round(((i.moving_time/60)/60), 0)
        distanceTotal.append(totalDistance)
        movingTotal.append(totalMoving)
        return [distanceTotal,
                movingTotal]


line_chart = TemplateView.as_view(template_name='chart.html')
line_chart_json = LineChartJSONView.as_view()
