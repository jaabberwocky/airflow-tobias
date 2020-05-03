import os
import datetime

def writefile(dag_run):
        '''
        Writes current dag run and timestamp to file.
        '''
        current_time = datetime.datetime.now().strftime('%B %d, %Y: %I:%M%p')
        formatted_string = f'DAG_RUN: {dag_run} || Current time: {current_time}\n'
        f = open(f'/home/airflow/out/{current_time}.txt', 'w')
        f.write(formatted_string)
        f.close()
