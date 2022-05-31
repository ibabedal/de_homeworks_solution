#!/bin/bash

## Prepare the pgadmin, notebook and postgres
mkdir ./notebooks ./pgvol ./pgadmin
chmod 777 ./pgadmin

## Prepare airflow setup
mkdir ./dags ./logs ./plugins ./af_pgvol ./db
echo -e "AIRFLOW_UID=$(id -u)\nAIRFLOW_GID=0" > .env
cp HW1_Q2_DAG.py ./dags/