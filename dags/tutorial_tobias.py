from datetime import timedelta
from airflow import DAG

from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago

default_args = {
    'owner':'tobias',
    'depends_on_past': False,
    'start_date': days_ago(2),
    'email' : 'tobias@dsaid.gov.sg',
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

dag = DAG(
    'tutorial_tobias',
    default_args=default_args,
    description="Simple tutorial DAG",
    schedule_interval = timedelta(minutes=5)
)

t1 = BashOperator(
    task_id = 'Append_timedate',
    bash_command = 'date +%Y%m%d:T%H%M%S >> /home/tobias/airflow/out/output.txt',
    dag=dag
)

t2 = BashOperator(
    task_id = 'sleep',
    bash_command = 'sleep 5',
    retries = 3,
    dag=dag
)

t3 = BashOperator(
    task_id = 'End',
    bash_command = 'echo Finished `date +%H:%M:%S`  >> /home/tobias/airflow/out/output.txt',
    dag=dag
)

t1 >> t2 >> t3