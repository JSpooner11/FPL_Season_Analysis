import requests
import csv

from getSeasonId import get_season_dates

url = 'https://fantasy.premierleague.com/api/fixtures/'

r = requests.get(url)

data = r.json()
matches = data
#matches = data['fixtures']

season_id = get_season_dates().strip()

def gather_match_data():
    with open("data/"+ season_id + "/match.csv", 'w', newline='') as file:
        header = ['id', 'kickoff_time', 'home_team', 'away_team', 'home_team_score', 'away_team_score', 'finished']
        writer = csv.DictWriter(file, fieldnames=header)
        writer.writeheader()
        
        id = 0

        for match in matches:
            id += 1
            match_data = {
                "id": id,
                "kickoff_time": match['kickoff_time'],
                "home_team": match['team_h'],
                "away_team": match['team_a'],
                "home_team_score": match['team_h_score'],
                "away_team_score": match['team_a_score'],
                "finished": match['finished']
            }
            writer.writerow(match_data)
            
gather_match_data()