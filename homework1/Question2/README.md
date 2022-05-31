# Solution for Question2 from homework1

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
- Please login to pgadmin http://localhost:8000 (username: deproject@proj.com, password: password123) to check on the data in the source database, details for connecting to the postgres server as below (it should be already connected, but just in case)
    - in case of an issue, the connection of pgadmin as below: server: **ibrahim_postgres** // username: postgres // password: password123 // DB: deproject
- Please login to the mongo-express http://localhost:8081 to check on the destination, the collection name is: **de_hw1**

---

## Q2 DAG detail:

#### The DAG contains 6 tasks that are explained as below:
- starting_point: a bash operator that echo a message indicating the start of workflow
- installing_dep: a python operator that installs the pymongo module for python as it is not installed by default.
  - NOTE: since we had 1 worker node in this example this would do the trick, if multiple worker nodes are there, a different method will be used to install the missing modules for python
- psqlTOdf: a python operator that will connect to the PostgresQL and will fetch the data from table "data" and return a pandas dataframe
- csvTOjson: a python operator that will read the returned (using airflow [XCOM](https://airflow.apache.org/docs/apache-airflow/stable/concepts/xcoms.html 'XCOM')) and will transfer it from its form into JSON List and return the generated list
- jsonTOmongo: a python operator that will read the returned JSON list (using XCOM also) and then transfer each json instance to mongodb database named "de_hw1" with collection called "jsonData"
- ending_point: a bash operator that echo a message indicating the end of the workflow

---

## Additional information:
- Below is a nice example on how to use the XCOM in airflow: https://marclamberti.com/blog/airflow-dag-creating-your-first-dag-in-5-minutes/
- Added the option "AIRFLOW__CORE__ENABLE_XCOM_PICKLING: 'true'" in the docker-compose file for airflow configuration to allow it to serialize non-JSON objects in the XCOM so that other tasks can read it ref: https://github.com/apache/airflow/issues/13487, https://stackoverflow.com/questions/65846976/passing-xcom-value-to-jiraoperator-in-airflow