from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView
from django.views.decorators.cache import cache_page
from .retrieve_club import retrieve_club
from .retrieve_data import retrieve
import datetime
from .models import Exercises


class LineChartJSONView(BaseLineChartView):
    def get_labels(self):
        names = []
        for i in Exercises.objects.all().order_by("id"):
            names.append(i.id)
        return names

    def get_providers(self):
        """Return names of datasets."""
        return ["Total Distance (KM)", "Total Time (Hours)"]

    def get_data(self):
        """Return 3 datasets to plot."""
        total_distance = 0
        distance_total = []
        total_moving = 0
        moving_total = []
        start_point = True
        for i in Exercises.objects.all().order_by("id"):
            total_distance += round(i.distance / 1000, 2)
            total_moving += round(((i.moving_time / 60)/60), 2)
            distance_total.append(total_distance)
            moving_total.append(total_moving)
        return [distance_total,
                moving_total]


main = TemplateView.as_view(template_name='main.html')
line_chart = TemplateView.as_view(template_name='chart.html')
map_view = TemplateView.as_view(template_name='map.html')
videos_view = TemplateView.as_view(template_name='videos.html')
line_chart_json = LineChartJSONView.as_view()
