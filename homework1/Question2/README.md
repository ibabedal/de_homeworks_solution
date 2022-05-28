# Question2 of homework1 solution

## Introduction to the current files:
- prepareenv.sh: a base script to create the needed folders that will be mounted on each container
- docker-compose.yml: the docker-compose file that contains the infrastructure build for airflow, postgres, mongodb and jupyter-lab containers
- HW1_Q2_DAG.py: the python file that contains the definition of the airflow DAG, details are in section (Q2 DAG detail), a copy of it is already exists in dags folder
- .env: needed for airflow impletmentaion to define the UID and GID
- notebooks: contains the notebook that is used to prepare the data in postgres so that airflow can fetch it(notebook name: hw1_q2_dataPrep.ipynb)
- dags: The folder that is used to save the DAGs in, so the airflow can use them, a copy for the solution DAG is already involved.

----

## Steps to prepare the environment and test the solution:
- Please run prepareenv.sh so that it will create the needed folders for implementation
- Please run "docker-compose up -d" so that the infrastructure containers are created
- Please login to http://localhost:8888 (secret: password123) to open the jupyter lab
- Please open the notebook named: hw1_q2_dataPrep.ipynb, and please execute teh cells to generate the data and push it postgres database
  - NOTE: Due to a bug in the libpq packages for Mac M1 laptops the connection to DB may fail, a workaround is to run the containers with [rosetta](https://docs.docker.com/desktop/mac/apple-silicon/#system-requirements 'rosetta')  or on intel based Linux machine ref link: https://stackoverflow.com/questions/62807717/how-can-i-solve-postgresql-scram-authentifcation-problem, https://github.com/MobSF/Mobile-Security-Framework-MobSF/issues/1898

- Please open http://localhost:8080 (username: airflow, password: airflow) and the DAG named HW1_Q2 should be there, please activate it and the workflow should start, more details about workflow in below section.

---

