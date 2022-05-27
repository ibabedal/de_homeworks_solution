from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
import datetime as dt
from datetime import timedelta
import pandas as pd
import numpy as np
from sqlalchemy import create_engine
import psycopg2

    
default_args={
    'owner': 'ibrahim',
    'start_date': dt.datetime(2022, 5, 27),
    'retries': 1,
    'retry_delay': dt.timedelta(minutes=5),
}

def PSQL_to_DF():
    host='ibrahim_postgres'
    username='postgres'
    password='password123'
    database='deproject'
    port='5432'
    engine = create_engine(f'postgresql://{username}:{password}@{host}:{port}/{database}')
    
    df = pd.read_sql('SELECT * FROM data', engine)
    
    return df.copy()

def CSV_to_JSON(df):
    df = df.xcom_pull(task_id='Read_from_DB')
    json_list = df.to_dict(orient='records')
    return json_list.copy()

def JSON_to_Mongo(data):
    from pymongo import MongoClient
    data = data.xcom_pull(task_id='Convert_to_Json')
    client = MongoClient('mongo-db:27017', username='root',password='example')
    db = client['de_hw1']
    collection = db.jsonData
    for i in range(0,len(data)):
        try:
            result = collection.insert_one(data[i])
        except:
            print(f'Error for reoord {i}')

            
with DAG('HW1_Q2',
         default_args=default_args,
         schedule_interval=timedelta(minutes=1),  
         catchup=False,     
         ) as dag:
    starting_point = BashOperator(task_id='starting_point', bash_command='echo "I am reading the CSV now....."')
    installing_dep = BashOperator(task_id='installing_dep', bash_command='pip install pymongo')
    #psqlTOdf = PythonOperator(task_id='Read_from_DB',python_callable=PSQL_to_DF)
    #csvTOjson = PythonOperator(task_id='Convert_to_Json',python_callable=CSV_to_JSON)
    #jsonTOmongo = PythonOperator(task_id='Write_to_Mongo',python_callable=JSON_to_Mongo)
    ending_point = BashOperator(task_id='ending_point', bash_command='echo "I am done with this DAG ^_^"')

#starting_point >> installing_dep >> psqlTOdf >> csvTOjson >> jsonTOmongo >> ending_point
starting_point >> installing_dep >> ending_point