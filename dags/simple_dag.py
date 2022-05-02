from airflow import DAG 
from airflow.operators.dummy import DummyOperator 


with DAG(dag_id='simple_dag', start_date=datetime(2021, 1, 1)) as dag: 
    task_1 = DummyOperator(
        task_id='task_1',
        start_date=datetime(2021, 1, 2)
    )


