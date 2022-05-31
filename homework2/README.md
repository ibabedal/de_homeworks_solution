# Solution for homework2

## Introduction to current files:
- docker-compose.yml: the docker-compose file that would create the infrastructure for this homework which is: airflow, postgres, pgadmin and jupyter notebook(the notebook is not needed, but I used it for testing)
- prepareenv.sh: the script that will prepare all of the needed folders for deploying the containers, copying the DAG to dags folder of airflow
- HW2_DAG.py: the DAG that is used to perform this workflow; details about it on the last section
- .env: needed file for airflow UID and GID
- pgadmin: the folder that will be loaded by the pgadmin and it has the connection already defined for the database.
    - in case of an issue, the connection of pgadmin as below: server: **ibrahim_hw2_homework2** // username: postgres // password: password123 // DB: deproject
- dags: the folder for dags of airflow, and it has the DAG python file already copied to it(it can be removed, the prepareenv.sh script will prepare it and ensure that the copy of python file for dag is already copied)
- notebooks: contains notebooks used while preparing the homework.

---

## Steps to prepare the environment and test the solution:
- Please run prepareenv.sh so that it will create the needed folders for implementation
- Please run "docker-compose up -d" so that the infrastructure containers are created
- Please login to the airflow http://localhost:8080 (username: airflow, password: airflow)
- Please click on the DAG **"HW2"**, then please enable it and hit on autorefresh and monitor the workflow.
    - NOTE: it would take some time to fetch the data from the github link (i.e the task **collect_files_for_uk**) depending on the internet speed
- Once the workflow completes, please open the pgadmin http://localhost:8000 (username: deproject@proj.com, password: password123) the connection should be there for the database, in case it is not please use the infromation above to connect to the DB and check on the table **uk_scoring_report**
- The csv file and the png both are on the folder that will be created called **output** 

---

## HW2 DAG detail:
starting_point >> installing_modules >> collect_files_for_uk >> scale_dataframe >> create_plot_and_csv >> send_dataframe_to_Postgres >> ending_point
#### the dag contains of 7 tasks explained as below:
- starting_point: a bash operator just to print that we are starting the workflow
- installing_modules: a bash operator that will install the sklean and matplot python modules
- collect_files_for_uk: a python operator that will collect the covid files from github, and filter for the **UK** as contry and **England** as a state, then return the unscaled dataset that will be saved in the task XCOM to be used later by other tasks
- scale_dataframe: a python operator that will receive the unscaled dataframe using (task instance and xcom_pull function - details below -) and load them into a dataframe, scale the data and return it.
- create_plot_and_csv: a python operator that will take the scaled dataframe and draw the plot and create a csv file that both will be saved on the **output** folder on the local machine
- send_dataframe_to_Postgres: a python operator that will send the scaled dataframe to the postgres database.

--- 

## Additional information:
- Below is a nice example on how to use the XCOM in airflow: https://marclamberti.com/blog/airflow-dag-creating-your-first-dag-in-5-minutes/
- Added the option "AIRFLOW__CORE__ENABLE_XCOM_PICKLING: 'true'" in the docker-compose file for airflow configuration to allow it to serialize non-JSON objects in the XCOM so that other tasks can read it ref: https://github.com/apache/airflow/issues/13487, https://stackoverflow.com/questions/65846976/passing-xcom-value-to-jiraoperator-in-airflow