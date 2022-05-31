#!/bin/bash

## Prepare the pgadmin, notebook and postgres
mkdir ./notebooks ./pgvol ./pgadmin
chmod 777 ./pgadmin

## Prepare airflow setup
mkdir ./dags ./logs ./plugins ./af_pgvol ./db ./output
echo -e "AIRFLOW_UID=$(id -u)\nAIRFLOW_GID=0" > .env
chmod 777 ./output
cp HW2_DAG.py ./dags/