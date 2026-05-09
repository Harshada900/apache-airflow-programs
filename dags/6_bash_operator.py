from airflow.operators.bash import BashOperator
from airflow.sdk import dag
#from airflow.providers.standard.operators.bash.BashOperator import BashOperator

@dag(
        dag_id="bash_op_dag",
        catchup=False
)
def bash_op_dag():
    ob = BashOperator(
        task_id="bash_op",
        bash_command ="echo 'Hello Python !'"
    )

bash_op_dag()