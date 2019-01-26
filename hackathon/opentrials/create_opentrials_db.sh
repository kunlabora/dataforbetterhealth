#!/bin/bash

docker-compose up --build -d

docker exec -i opentrials_db_1 pg_restore -C --clean --no-acl --no-owner -U postgres -d postgres < opentrials-api-2018-04-01.dump 
