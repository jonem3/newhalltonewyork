import requests
import json
from datetime import datetime
import time

def retrieve():

    startdate = "01-05-2020 00:00:00"
    startdate = time.strptime(startdate, "%d-%m-%Y %H:%M:%S")
    startdate = int(time.mktime(startdate))

    auth_url = "https://www.strava.com/oauth/token"
    payload = {
            'client_id': "47934",
            'client_secret': 'bfbff2207fa852c433896f821250dda04a418bf9',
            'refresh_token': '1aaf804d13502cf85759fe0f1a4f03f538f1a80d',
            'grant_type': 'refresh_token',
            'f': 'json'
        }
    """
    payload = {
        'client_id': "47934",
        'client_secret': 'bfbff2207fa852c433896f821250dda04a418bf9',
        'code': 'f02d38ae96666cd940f1003bee42070351a390cc',
        'grant_type': 'authorization_code'
    }
    """
    res = requests.post(auth_url, data=payload, verify=False)
    #print(res.json())
    access_token = res.json()['access_token']
    url = "https://www.strava.com/api/v3/athlete/activities?access_token={}".format(access_token)
    param = {'per_page': 200, 'page': 1, 'after': startdate}
    obs_r = requests.get(url, params=param)
    obs_status = obs_r.status_code
    if 200 <= obs_status < 300:
        obs_data = json.loads(obs_r.text)
    else:
        obs_data = obs_status
        print(obs_data)
    return obs_data