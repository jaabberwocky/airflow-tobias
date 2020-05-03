from airflow import DAG
from airflow.contrib.sensors.file_sensor import FileSensor
from airflow.operators.bash_operator import BashOperator
from datetime import date, timedelta, datetime


DAG_DEFAULT_ARGS = {
        'owner':'tobias',
        'depends_on_past':False,
        'retries':1,
        'retry_delay': timedelta(minutes=1),
        'start_date':datetime(2020,5,1)
}

dag = DAG(
        'sensor_dag',
        default_args = DAG_DEFAULT_ARGS,
        description = 'Simple tutorial to use filesensors',
        schedule_interval = '*/1 * * * *',
        catchup = False
)

t1 = FileSensor(
        task_id = 'check_file',
        fs_conn_id='fs_default',
        filepath='/home/airflow/airflow_files/nice.txt',
        poke_interval=5,
        dag = dag
)

t2 = BashOperator(
        task_id = 'write_file',
        bash_command = 'echo See the file at `date +%Y%m%dT%H:%M:%S` >> /home/airflow/airflow/out/nice_log.txt',
        retries = 1,
        dag=dag
)

t1 >> t2