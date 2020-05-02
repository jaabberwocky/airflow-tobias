#!/bin/bash

echo "Starting scheduler..."
airflow scheduler &
echo "Starting server..."
airflow webserver -p 8080 &
echo "All done!"
