from airflow.sdk import dag
from airflow.operators.bash import BashOperator
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator

@dag(
    dag_id="jinja_with_operators",
    catchup=False,
    schedule=None
)
def jinja_with_operators():

    #bash
    print_data = BashOperator(
        task_id="print_data",
        bash_command="""
        echo "Today is {{ds}}"
        echo "Dag name is {{dag.dag_id}}"

    """
    )

    fetch_data = SQLExecuteQueryOperator(
        task_id="fetch_data",
        conn_id="my_postgres",      #it will failed bcz therrs no cnnection 
        sql="""
        select *
        from sales
        where date = '{{ds}}' AND
        dag_run = '{{run_id}}'

    """
    )
    print_data >> fetch_data

jinja_with_operators()

