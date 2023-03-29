from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 3, 21),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'neo4j_pipeline',
    default_args=default_args,
    description='Orchestrates the pipeline to load XML data into Neo4j',
    schedule_interval='@daily',
)

# Task 1: Parse the XML file
task1 = BashOperator(
    task_id='parse_xml',
    bash_command='python /Users/ritvikraj/airflow/dags/parse_xml.py',
    dag=dag,
)

# Task 2: Transform the data
task2 = BashOperator(
    task_id='transform_data',
    bash_command='python /Users/ritvikraj/airflow/dags/transform_data.py',
    dag=dag,
)

# Task 3: Load data into Neo4j
task3 = BashOperator(
    task_id='load_neo4j',
    bash_command='python /Users/ritvikraj/airflow/dags/load_neo4j.py',
    dag=dag,
)

# Set dependencies between tasks
task1 >> task2 >> task3
