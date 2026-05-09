from airflow.operators.python import PythonOperator
from airflow.sdk import dag
def my_function():
    print("Python function running")

@dag(
    dag_id='python_op_dag',
    catchup= False,
)
def python_op_dag():

    ob = PythonOperator(
        task_id = "run_python",
        python_callable = my_function
    )                                       #@task does the same !
python_op_dag()