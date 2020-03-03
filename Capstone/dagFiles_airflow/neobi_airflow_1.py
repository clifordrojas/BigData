from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

# Following are defaults which can be overridden later on
default_args: dict = {
    'owner': 'Cliford',
    'depends_on_past': False,
    'start_date': datetime(2020, 3, 1),
    'email': ['cliford.rojas@enhanceit.us'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 0,
    'retry_delay': timedelta(minutes=1),
}

dag:DAG = DAG( 'neobi_dependencies',
           default_args=default_args,
           schedule_interval=timedelta(hours=24)
         )

# Bash Commands for Pipeline

run_dependency = BashOperator( task_id='run_dependency',
                          bash_command='. ~/Desktop/BigData/Capstone/Automation/run_dependencies_first.sh ',
                          dag=dag
                        )
run_ncy = BashOperator( task_id='run_ncy',
                          bash_command='pwd',
                          dag=dag
                        )





run_dependency.set_downstream(run_ncy)
