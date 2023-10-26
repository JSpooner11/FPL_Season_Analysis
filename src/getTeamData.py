import requests
import csv

from getSeasonId import get_season_dates

url = 'https://fantasy.premierleague.com/api/bootstrap-static/'

r = requests.get(url)

data = r.json()
teams = data["teams"]

season_id = get_season_dates().strip()

def gather_team_data():
    with open("data/"+ season_id + "/team.csv", 'w', newline='') as file:
        header = ['id', 'name', 'strength', 'season']
        writer = csv.DictWriter(file, fieldnames=header)
        writer.writeheader()
        
        id = 0

        for team in teams:
            id += 1
            team_data = {
                "id": id,
                "name": team['name'],
                "strength": team['strength'],
                "season": season_id
            }
            writer.writerow(team_data)
            

gather_team_data()