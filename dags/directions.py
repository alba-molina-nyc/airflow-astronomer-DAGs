# Step 1 - import dag class - used in order to instantiate a DAG object 
from airflow import DAG 
# Step 4 - import the operator (the dummy operator is an operator that does nothing so it is good for experiments)
from airflow.operators.dummy import DummyOperator 
# Step 6 - import date time object
from datetime import datetime

# Step 2 - instantiate the DAG object - you can do it by creating a variable

# dag = (DAG...)
# task_1 = Operator(dag=dag)

# But a cleaner way to do step 2 is: 

# with DAG(...) as dag: 
#     task_1 = Operator()

# Step 3 - add the dag_id , # Step 7 - add start_date
with DAG(dag_id='simple_dag', start_date=datetime(2021, 1, 1)) as dag: 
    # Step 5 - create the first task 
    task_1 = DummyOperator(
        task_id='task_1'
    )

# START DATE- when your dag starts being scheduled 
# & SCHEDULE INTERVAL- defines the frequency at which your dag will be triggered
# your dag is triggered once both the start & the schedule interval have elapsed
# END DATE- defines the date at which your dag won't be scheduled anymore