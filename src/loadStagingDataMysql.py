import mysql.connector as msql
import csv
import pandas as pd

#get docker ip
#docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' mysqlLocal

# Connect to the database
conn = msql.connect(host='172.21.0.2', user='root', password='root', database='staging_football_stats')
mycursor = conn.cursor()

team_csv = 'data/2023-24/team.csv'
player_stats_csv = 'data/2023-24/player_stats.csv'
fixtures_csv = 'data/2023-24/match.csv'

mycursor.execute('TRUNCATE team;')
mycursor.execute('TRUNCATE player_stats;')
mycursor.execute('TRUNCATE fixtures;')

team_list = list()
with open(team_csv, mode="r") as csv_reader:
    csv_reader = csv.reader(csv_reader)
    next(csv_reader)
    for rows in csv_reader:
        team_list.append({'id':rows[0], 'name':rows[1], 'strength':rows[2], 'season':rows[3]})
        
for item in team_list:
    sql = "INSERT INTO team(team_id, team_name, team_strength, season) VALUES (%s, %s, %s, %s)"
    val = item['id'], item['name'], item['strength'], item['season']
    mycursor.execute(sql, val)
conn.commit()

player_stats_list = list()
with open(player_stats_csv, mode="r") as csv_reader:
    csv_reader = csv.reader(csv_reader)
    next(csv_reader)
    for rows in csv_reader: 
        player_stats_list.append({'game_id':rows[0],'match_date':rows[1],'home_team':rows[2],'away_team':rows[3],'score':rows[4],'goal_scorer_h':rows[5],'goal_min_h':rows[6],'goal_scorer_a':rows[7],'goal_min_a':rows[8],'event_type':rows[9]})
        
for item in player_stats_list:
    sql = "INSERT INTO player_stats(stat_id, home_team, away_team, score, event_player_h, event_min_h, event_player_a, event_min_a, event_type) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val = item['game_id'],item['home_team'],item['away_team'],item['score'],item['goal_scorer_h'],item['goal_min_h'],item['goal_scorer_a'],item['goal_min_a'],item['event_type']
    mycursor.execute(sql, val)
conn.commit()

fixtures_list = list()
with open(fixtures_csv, mode="r") as csv_reader:
    csv_reader = csv.reader(csv_reader)
    next(csv_reader)
    for rows in csv_reader:
        fixtures_list.append({'id':rows[0], 'kickoff_time':rows[1], 'home_team':rows[2], 'away_team':rows[3], 'home_team_score':rows[4], 'away_team_score':rows[5], 'finished':rows[6]})
        
for item in fixtures_list:
    sql = "INSERT INTO fixtures(fixture_id, kickoff_time, home_team, away_team, home_team_score, away_team_score, finished) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    val = item['id'], item['kickoff_time'], item['home_team'], item['away_team'], item['home_team_score'], item['away_team_score'], item['finished']
    mycursor.execute(sql, val)
conn.commit()

mycursor.execute('SELECT * FROM team')
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

conn.close()

