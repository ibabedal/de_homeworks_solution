#!/bin/bash


echo 'Creating the needed folders to used for nifi ..'
mkdir ./data
chmod 777 ./data

echo 'copying the csv2json.py script that would be used in nifi workflow'
cp csv2json.py ./data
chmod +x ./data/csv2json

echo 'Copying data.csv to ./data'
cp data.csv ./data

echo 'Starting up the environment ..'
docker-compose up -d

echo "We need to install the python interpreter and pands model as they are not installed"
docker exec -u 0 -it ibrahim_nifi_dataenv apt-get update
docker exec -u 0 -it ibrahim_nifi_dataenv apt-get install -y python3 python3-pip
docker exec -u 0 -it ibrahim_nifi_dataenv pip3 install pandas numpy

echo 'we are done ,wait for almost a min for nifi to initialize the you can use it ..'