import pytz
import requests
import json
from .models import Exercises
from django.utils import timezone
from datetime import datetime
import time


def retrieve_club():
    auth_url = "https://www.strava.com/oauth/token"
    payload = {
        'client_id': "47934",
        'client_secret': 'bfbff2207fa852c433896f821250dda04a418bf9',
        'refresh_token': '1aaf804d13502cf85759fe0f1a4f03f538f1a80d',
        'grant_type': 'refresh_token',
        'f': 'json'
    }
    res = requests.post(auth_url, data=payload, verify=False)
    # print(res.json())
    access_token = res.json()['access_token']
    url = "https://www.strava.com/api/v3/clubs/662071/activities"
    obs_data_complete = ""
    for i in range(0, 8):
        param = {'per_page': 200, 'page': i}
        header = {"Authorization": "Bearer " + access_token}
        obs_r = requests.get(url, headers=header, params=param)
        obs_status = obs_r.status_code
        if 200 <= obs_status < 300:
            obs_data_complete += obs_r.text
        else:
            obs_data = obs_status
            print(obs_data)
    obs_data_complete = obs_data_complete.replace("[]", "")
    obs_data_complete = obs_data_complete.replace("][", ",")
    #print(len(json.loads(obs_data_complete)))
    #return (obs_data_complete)
    obs_data_complete = json.loads(obs_data_complete)
    #print(timezone.localtime(timezone.now()))
    #start_point = True
    try:
        for i in reversed(obs_data_complete):

            #if not start_point:
            exercise = Exercises.objects.filter(
                name=i['name'],
                distance=i['distance'],
                moving_time=i['moving_time'],
                total_elevation_gain=i['total_elevation_gain']).first()
            if not exercise:
                exercise = Exercises()
                exercise.name = i['name']
                exercise.distance = i['distance']
                exercise.moving_time = i['moving_time']
                exercise.total_elevation_gain = i['total_elevation_gain']
                timezone.activate(pytz.timezone("Europe/London"))
                exercise.time_stamp = timezone.localtime(timezone.now())
                exercise.save()

            # if start_point:
            #     if i['athlete']['firstname'] == "Matthew" and i['name'] == "Flitch Way Dunmow - Stansted" and float(
            #             i['distance']) == 22410.1:
            #         start_point = False
    except Exception as e:
        pass