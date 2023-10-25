import requests
import csv

url = 'https://fantasy.premierleague.com/api/bootstrap-static/'

r = requests.get(url)

data = r.json()
teams = data["teams"]

def gather_team_data():
    with open("data/2023-24/team.csv", 'w', newline='') as file:
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
                "season": '2023-24'
            }
            writer.writerow(team_data)

gather_team_data()
