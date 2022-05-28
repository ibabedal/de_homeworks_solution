# Question2 of homework1 solution

## Introduction to the current files:
- prepareenv.sh: a base script to create the needed folders that will be mounted on each container
- docker-compose.yml: the docker-compose file that contains the infrastructure build for airflow, postgres, mongodb and jupyter-lab containers
- HW1_Q2_DAG.py: the python file that contains the definition of the airflow DAG, details are in section (Q2 DAG detail), a copy of it is already exists in dags folder
- .env: needed for airflow impletmentaion to define the UID and GID
- notebooks: contains the notebook that is used to prepare the data in postgres so that airflow can fetch it(notebook name: hw1_q2_dataPrep.ipynb)
- dags: The folder that is used to save the DAGs in, so the airflow can use them, a copy for the solution DAG is already involved.

----

