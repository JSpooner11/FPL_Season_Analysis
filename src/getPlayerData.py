import requests
import csv
from bs4 import BeautifulSoup

# To do: https://fbref.com/en/comps/9/schedule/Premier-League-Scores-and-Fixtures
# Set out data like: 
# gw, team_h, team_a, team_h_scorer, team_a_scorer, score, goal_minute
# 1 , bur, man-city, false, true, haaland, 1-0, 4
# 1 , bur, man-city, false, true, haaland, 2-0, 19

## /en/matches/3a6836b4/Burnley-Manchester-City-August-11-2023-Premier-League - This is from href I can append this to get goal info
## https://fbref.com/en/matches/3a6836b4/Burnley-Manchester-City-August-11-2023-Premier-League (This API I can use to get goal scorers)

def clean_scorer_data(item):
    parts = item.split("·")
    if len(parts) == 2:
        player_name = parts[0].strip()
        minute = parts[1].strip()
        return player_name, minute
    else:
        return None


url = "https://fbref.com/en/comps/9/schedule/Premier-League-Scores-and-Fixtures"
response = requests.get(url)

html_content = requests.get(url).text

if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, "html.parser")

    # Find the table containing the match data
    table = soup.find("table", {"class": "stats_table"})

    # Extract match data from the table
    match_data = []
    cleaned_goals_data = []
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
            #print(goal_scorer_url)
            
            goal_scorer_response = requests.get(goal_scorer_url)
            #print(goal_scorer_response)

            goal_scorer_html_content = requests.get(goal_scorer_url).text
            
            if goal_scorer_response.status_code == 200:
                goal_scorer_soup = BeautifulSoup(goal_scorer_response.text, "html.parser")
                
            parent_div = goal_scorer_soup.find("div", {"id": "b"})

                
            #scorer_data = []

            for div in parent_div:  
                away_scoerer_and_time = div.find_next("div").text.strip()
                if len(away_scoerer_and_time) > 0:
                    print(away_scoerer_and_time)
                    cleaned_goals_data.append(away_scoerer_and_time)      
            
            goalcsv = open("data/2023-24/goal_scorers.txt", "a")
            for item in cleaned_goals_data:
                goalcsv.write(str(item))
            #f.write(str(cleaned_goals_data))
        
            #cleaned_data = [clean_scorer_data(item) for item in scorer_data]    
            #cleaned_data = [item for item in cleaned_data if item is not None]  

            #clean_scorer_data.append()   

        match_data.append((match_date, home_team, score, away_team, href))
                
                
    # Print the extracted match data
    matchcsv = open("data/2023-24/match_new.txt", "a")
    for match in match_data:
        matchcsv.write(str(match))
        #print(match)

