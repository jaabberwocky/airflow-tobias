from airflow import DAG
from datetime import timedelta, datetime, date
from airflow.operators.python_operator import PythonOperator

import write_date

default_args = {

        'owner':'tobias',
        'depends_on_past': False,
        'email':'tobias@dsaid.gov.sg',
        'retries':1,
        'retry_delay': timedelta(minutes=5),
        'start_date': datetime(2020, 5, 1)
}

dag = DAG(
        'template_dag',
        default_args = default_args,
        description = 'Simple tutorial dag to use Jinja templates',
        schedule_interval = '*/5 * * * *',
        catchup=False
)

def say_hello():
        print("Hello!")


t1 = PythonOperator(
        task_id = 'Say_hello',
        python_callable=say_hello,
        dag=dag
)

t2 = PythonOperator(
        task_id = 'Write_date',
        python_callable = write_date.writefile,
        op_args = ['{{ run_id }}'],
        dag=dag
)

t1 >> t2