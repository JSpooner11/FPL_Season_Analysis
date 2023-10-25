CREATE DATABASE dw_football_stats;

CREATE TABLE IF NOT EXISTS dim_team (
    team_id INT,
    team_name (VACHAR(35))
);

CREATE TABLE dim_match (
    match_id INT,
    home_team VARCHAR(35),
    away_team VARCHAR(35)
);

