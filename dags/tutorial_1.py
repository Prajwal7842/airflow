import textwrap
from datetime import datetime, timedelta

from airflow.models.dag import DAG

from airflow.operators.bash import BashOperator

with DAG(
    'tutorial_bash',
    default_args = {
        "depends_on_past": False,
        "email": ['prajwalgoel@gnail.com'],
        'email_on_failure': False,
        'email_on_retry': False,
        'retries': 1,
        'retry_delay': timedelta(1),
    },
    description= 'First example dag from tutorial',
    schedule= timedelta(minutes=10),
    start_date=datetime(2025, 3, 25),
    catchup=False,
    tags=["example"],  
) as dag:
    t1 = BashOperator(
        task_id='print_date',
        bash_command='date'
    )

    t2 = BashOperator(
        task_id='sleep',
        depends_on_past=False,
        bash_command='sleep 10',
        retries=3
    )

    t1 >> t2
    
