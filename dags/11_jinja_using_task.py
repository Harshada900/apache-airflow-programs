from airflow.sdk import dag, task
import pendulum

@dag(
    dag_id="jinja_example",
    catchup=False,
    schedule=None
)
def jinja_example():

    @task
    def fetch_data(**context):      #we use context to access macros/jinja

        run_date = context['ds']
        

        print(f"running date is {run_date}")

        sql = f"select * from emp where date = '{run_date}'" 

        print(sql)
    fetch_data()

jinja_example()