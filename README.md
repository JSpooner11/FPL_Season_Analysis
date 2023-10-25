# FPL-Season-Analysis

## Docker
1. Create a Docker-compose File.
2. Ability to Spin up Docker with SQL.

### How to:
1. Spin up Docker
`sudo docker-compose up -d`

2. Access Mysql Container
`sudo docker exec -it mysqlLocal /bin/bash`

3. Use Mysql
`mysql -uroot -proot`

4. Create DDL
The DDL gets create on docker init.


## SQL 
1. Create Schemas on SQL Docker.
2. Have a Star Schema to Analyse the Data (DW).

## Python
1. Hit a PL API and pull down the data.
2. Transform and Cleanse the data.
3. Insert the data into a staging layer.
4. Then Insert the data into the DW. 
