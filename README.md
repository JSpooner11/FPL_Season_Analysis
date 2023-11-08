# FPL-Season-Analysis

## Docker
1. Create a Docker-compose File.
2. Ability to Spin up Docker with SQL.

### Run Docker Locally:
1. Spin up Docker
`sudo docker-compose up -d`

2. Access Mysql Container
`sudo docker exec -it mysqlLocal /bin/bash`

3. Use Mysql
`mysql -uroot -proot`

4. Create DDL
The DDL gets create on docker init.

5. Get Docker IP address
`docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' mysqlLocal`

### Docker Gotchas
If you change SQL scripts you might need to docker-compose down, remove volumes.
`ERROR 1045 (28000): Access denied for user 'root'@'localhost' (using password: YES)`

`
docker volume ls
docker volume rm volume_name
`

## SQL 
1. Create Schemas on SQL Docker.
2. Have a Star Schema to Analyse the Data (DW).

## Python
1. Hit a PL API and pull down the data.
2. Transform and Cleanse the data.
3. Insert the data into a staging layer.
4. Then Insert the data into the DW. 


# How To: 
1. Installing SQLFluff 
`pip install sqlfluff`
2. Installing pre-commit
`pip install pre-commit`
3. Running pre-commit
    Install pre-commit to work with git commit:
    `pre-commit install`
    Run pre-commit on all files:
    `pre-commit run --all-files`