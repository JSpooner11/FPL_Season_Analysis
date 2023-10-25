CREATE DATABASE dw_football_stats;

CREATE TABLE IF NOT EXISTS dw_football_stats.dim_team (
    team_id INT,
    team_name VARCHAR(35)
);

CREATE TABLE IF NOT EXISTS dw_football_stats.dim_match (
    match_id INT,
    home_team VARCHAR(35),
    away_team VARCHAR(35)
);
