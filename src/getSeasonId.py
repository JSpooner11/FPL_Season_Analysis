import requests
import csv

url = 'https://fantasy.premierleague.com/api/bootstrap-static/'

r = requests.get(url)

data = r.json()
events = data["events"]

def get_season_dates():
    gw1_event = events[0]
    gw1_date = gw1_event["deadline_time"]
    gw1_start_year = gw1_date[0:4]
    gw1_end_year = int(gw1_date[2:4])+1
    season_id = gw1_start_year + "-" + str(gw1_end_year)

    return season_id