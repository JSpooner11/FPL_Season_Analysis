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
csv_writer.writerow(['game_id', 'match_date', 'home_team', 'away_team', 'score', 'goal_scorer_h', 'goal_min_h', 'goal_scorer_a', 'goal_min_a', 'event_type'])

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    table = soup.find("table", {"class": "stats_table"})
    
    game_id = 1

    for row in table.find_all("tr")[1:]:
        game_id += 1 
        cells = row.find_all("td")
        match_date = cells[1].text.strip()
        home_team = cells[3].text.strip()
        score = cells[5].text.strip()
        away_team = cells[7].text.strip()
        score_cell = cells[5]
        href = score_cell.find("a")["href"] if score_cell.find("a") else None
        
        if score != '0–0':
        
            if href != None:
                goal_scorer_url = "https://fbref.com" + str(href).strip()
                
                # 6 secs delay to comply with fbref requests guidelines (20 requests a min)
                time.sleep(6)
                
                goal_scorer_response = requests.get(goal_scorer_url)

                goal_scorer_html_content = requests.get(goal_scorer_url).text
                
                if goal_scorer_response.status_code == 200:
                    goal_scorer_soup = BeautifulSoup(goal_scorer_response.text, "html.parser")
                    
                    try:
                    
                        parent_div = goal_scorer_soup.find('div', class_='event', id='a')

                        for div in parent_div:  
                            home_scoerer_and_time = div.text.strip()
                            event_type = div.find_next('div').attrs
                            if len(home_scoerer_and_time) > 0:
                                home_scoerer_and_time = home_scoerer_and_time.split('·')
                                goal_scorer_h = home_scoerer_and_time[0].strip()
                                goal_min_h = home_scoerer_and_time[1].strip().replace('’', '')
                                event_type = event_type['class'][1]
                                csv_writer.writerow([game_id, match_date, home_team, away_team, score, goal_scorer_h, goal_min_h, None, None, event_type])    
                    
                    except Exception as e: 
                        pass
                
                    try:
                        
                        parent_div = goal_scorer_soup.find('div', class_='event', id='b')

                        for div in parent_div:  
                            away_scoerer_and_time = div.text.strip()
                            event_type = div.find_next('div').attrs
                            if len(away_scoerer_and_time) > 0:
                                away_scoerer_and_time = away_scoerer_and_time.split('·')
                                goal_scorer_a = away_scoerer_and_time[0].strip()
                                goal_min_a = away_scoerer_and_time[1].strip().replace('’', '')
                                event_type = event_type['class'][1]
                                csv_writer.writerow([game_id, match_date, home_team, away_team, score, None, None, goal_scorer_a, goal_min_a, event_type])    
                    
                    except Exception as e:
                        pass
                    
        else:
            csv_writer.writerow([game_id, match_date, home_team, away_team, score, None, None, None, None, None])  
        


