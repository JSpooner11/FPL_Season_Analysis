import requests
import csv
import time
from bs4 import BeautifulSoup

from getSeasonId import get_season_dates

url = "https://fbref.com/en/comps/9/schedule/Premier-League-Scores-and-Fixtures"

response = requests.get(url)

html_content = requests.get(url).text   

season_id = get_season_dates().strip()

csv_file = open('data/' + season_id + '/player_stats.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['match_date', 'home_team', 'away_team', 'score', 'goal_scorer_h', 'goal_min_h', 'goal_scorer_a', 'goal_min_a'])

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    table = soup.find("table", {"class": "stats_table"})

    for row in table.find_all("tr")[1:]:
        cells = row.find_all("td")
        match_date = cells[0].text.strip()
        home_team = cells[3].text.strip()
        score = cells[5].text.strip()
        away_team = cells[7].text.strip()
        score_cell = cells[5]
        href = score_cell.find("a")["href"] if score_cell.find("a") else None
        
        if href != None:
            goal_scorer_url = "https://fbref.com" + str(href).strip()
            
            #wait 6 secs to for fbref more than 1 request every 3 secs
            time.sleep(6)
            
            goal_scorer_response = requests.get(goal_scorer_url)

            goal_scorer_html_content = requests.get(goal_scorer_url).text
            
            if goal_scorer_response.status_code == 200:
                goal_scorer_soup = BeautifulSoup(goal_scorer_response.text, "html.parser")
                
                try:
                
                    parent_div = goal_scorer_soup.find("div", {"id": "a"})

                    for div in parent_div:  
                        home_scoerer_and_time = div.find_next("div").text.strip()
                        if len(home_scoerer_and_time) > 0:
                            home_scoerer_and_time = home_scoerer_and_time.split('·')
                            goal_scorer_h = home_scoerer_and_time[0].strip()
                            goal_min_h = home_scoerer_and_time[1].strip()
                            csv_writer.writerow([match_date, home_team, away_team, score, goal_scorer_h, goal_min_h, None, None])    
                
                except Exception as e: 
                    pass
            
                try:
                    
                    parent_div = goal_scorer_soup.find("div", {"id": "b"})

                    for div in parent_div:  
                        away_scoerer_and_time = div.find_next("div").text.strip()
                        if len(away_scoerer_and_time) > 0:
                            away_scoerer_and_time = away_scoerer_and_time.split('·')
                            goal_scorer_a = away_scoerer_and_time[0].strip()
                            goal_min_a = away_scoerer_and_time[1].strip()
                            csv_writer.writerow([match_date, home_team, away_team, score, None, None, goal_scorer_a, goal_min_a])    
                
                except Exception as e:
                    csv_writer.writerow([match_date, home_team, away_team, score, None, None, None, None])  
        


