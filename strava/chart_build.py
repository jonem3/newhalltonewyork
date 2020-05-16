from django.http import JsonResponse
from .models import Exercises
from django.views.decorators.cache import cache_page

TOTAL_DISTANCE = "Total Distance (KM)"
TOTAL_TIME = "Total Time (Hours)"


@cache_page(500)
def chart_json(request):
    names = []
    total_distance = 0
    distances = []
    total_moving = 0
    times = []
    start_point = True

    for i in Exercises.objects.all().order_by("id"):
        total_distance += i.distance / 1000
        total_moving += (i.moving_time / 60) / 60
        distances.append(round(total_distance, 2))
        times.append(round(total_moving, 2))
        names.append(round(total_distance, 0))

    jason = {
        "labels": names,
        "datasets": [
            {
                "yAxisID": TOTAL_DISTANCE,
                "label": TOTAL_DISTANCE,
                "data": distances,
                "name": TOTAL_DISTANCE,
                "backgroundColor": "rgba(51, 102, 255, 0.5)",
                "borderColor": "rgba(51, 102, 255, 1)",
                "pointBackgroundColor": "rgba(51, 102, 255, 1)",
                "pointBorderColor": "#fff",
            },
            {
                "yAxisID": TOTAL_TIME,
                "label": TOTAL_TIME,
                "data": times,
                "name": TOTAL_TIME,
                "backgroundColor": "rgba(171, 9, 0, 0.7)",
                "borderColor": "rgba(171, 9, 0, 1)",
                "pointBackgroundColor": "rgba(171, 9, 0, 1)",
                "pointBorderColor": "#fff",
            }
        ]
    }
    return JsonResponse(jason)

