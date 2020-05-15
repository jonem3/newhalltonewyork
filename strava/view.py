from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView
from .retrieve_data import retrieve
import datetime

class LineChartJSONView(BaseLineChartView):
    def get_labels(self):
        data = retrieve()
        timestamps = []
        for i in data:
            timestamps.append(datetime.datetime.strptime(i['start_date'], '%Y-%m-%dT%H:%M:%SZ'))
        """Return 7 labels for the x-axis."""
        return timestamps

    def get_providers(self):

        """Return names of datasets."""
        return ["Total Distance (KM)", "Total Time (Hours)"]

    def get_data(self):
        """Return 3 datasets to plot."""
        data = retrieve()
        totalDistance = 0
        distanceTotal = []
        totalMoving = 0
        movingTotal = []
        for i in data:
            totalDistance += round(i['distance']/1000, 2)
            distanceTotal.append(totalDistance)
            totalMoving += round(((i['moving_time']/60)/60), 0)
            movingTotal.append(totalMoving)
        return [distanceTotal,
                movingTotal]


line_chart = TemplateView.as_view(template_name='chart.html')
line_chart_json = LineChartJSONView.as_view()
