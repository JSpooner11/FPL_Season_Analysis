CREATE DATABASE staging_football_stats;

CREATE TABLE IF NOT EXISTS staging_football_stats.fixtures (
    fixture_id INT,
    kickoff_time DATETIME,
    home_team VARCHAR(35),
    away_team VARCHAR(35),
    home_team_score INT,
    away_team_score INT,
    finished BOOLEAN
);

CREATE TABLE IF NOT EXISTS staging_football_stats.player_stats (
    stat_id INT,
    fixture_id INT,
    home_team VARCHAR(35),
    away_team VARCHAR(35),
    score VARCHAR(4),
    event_player_h VARCHAR(50),
    event_min_h CHAR(4),
    event_player_a VARCHAR(50),
    event_min_a CHAR(4),
    event_type VARCHAR(20)
);

CREATE TABLE IF NOT EXISTS staging_football_stats.team (
    team_id INT,
    team_name VARCHAR(35),
    team_strength INT,
    season VARCHAR(7)
);
