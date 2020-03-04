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
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

dag:DAG = DAG( 'neobi_dag',
           default_args=default_args,
           schedule_interval=timedelta(hours=1)
         )

# Bash Commands for Pipeline

mk_h_table = BashOperator( task_id='mk_h_table',
                          bash_command='. ~/Desktop/BigData/Capstone/Automation/run_hive_mkTable.sh ',
                          dag=dag
                        )

run_ingest = BashOperator( task_id='run_ingest',
                          bash_command='. ~/Desktop/BigData/Capstone/Automation/run_ingestion.sh ',
                          dag=dag
                        )

mv_data = BashOperator( task_id='mv_data',
                          bash_command='. ~/Desktop/BigData/Capstone/Automation/move_data_hdfs.sh ',
                          dag=dag
                        )


spark_process = BashOperator( task_id='spark_process',
                          bash_command='. ~/Desktop/BigData/Capstone/Automation/process_data.sh ',
                          dag=dag
                        )

give_hive_data = BashOperator( task_id='give_hive_data',
                          bash_command='. ~/Desktop/BigData/Capstone/Automation/load_data_hive.sh ',
                          dag=dag
                        )



mk_h_table.set_downstream(run_ingest)

#run > mv data > spark_process
run_ingest.set_downstream(mv_data)
mv_data.set_downstream(spark_process)

# spark > give hive data
spark_process.set_downstream(give_hive_data)
