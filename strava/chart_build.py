from django.http import JsonResponse
from .models import Exercises
from django.views.decorators.cache import cache_page

TOTAL_DISTANCE = "Total Distance (KM)"
TOTAL_TIME = "Total Time (Hours)"
TOTAL_REMAINING = "Total Distance Remaining (KM)"
OVERALLDISTANCE = 5617


@cache_page(500)
def chart_json(request):
    names = []
    total_distance = 0
    distances = []
    total_moving = 0
    times = []
    start_point = True

    for i in Exercises.objects.all().order_by("time_stamp"):
        total_distance += i.distance / 1000
        total_moving += (i.moving_time / 60) / 60
        distances.append({'t': i.time_stamp, 'y': round(total_distance, 2)})
        times.append({'t': i.time_stamp, 'y': round(total_moving, 2)})
        #names.append(round(total_distance, 0))
        names.append(i.time_stamp)

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

@cache_page(500)
def distances_json(request):

    total_distance = 0
    total_remaining = 0
    start_point = True

    for i in Exercises.objects.all().order_by("id"):
        total_distance += i.distance / 1000
    total_remaining = 5614 - total_distance
    remaining_total = [total_remaining]
    distance_total = [total_distance]
    names = [str(total_distance)+"/"+str(total_remaining)]
    jason = {
        "labels": names,
        "datasets": [
            {
                "label": TOTAL_DISTANCE,
                "data": distance_total,
                "name": TOTAL_DISTANCE,
                "backgroundColor": "rgba(51, 102, 255, 0.5)",
                "borderColor": "rgba(51, 102, 255, 1)",
                "pointBackgroundColor": "rgba(51, 102, 255, 1)",
                "pointBorderColor": "#fff",
            },
            {
                "label": TOTAL_REMAINING,
                "data": remaining_total,
                "name": TOTAL_REMAINING,
                "backgroundColor": "rgba(171, 9, 0, 0.7)",
                "borderColor": "rgba(171, 9, 0, 1)",
                "pointBackgroundColor": "rgba(171, 9, 0, 1)",
                "pointBorderColor": "#fff",
            }
        ]
    }
    return JsonResponse(jason)
