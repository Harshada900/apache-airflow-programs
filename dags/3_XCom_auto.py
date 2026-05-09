from airflow.sdk import dag, task

@task
def task_a()-> int:
    return 42                   #automatically pushed(saved) to Airflow's XCom database

@task
def task_b(num: int):
    print(num)                 #automatically pulled(fetched) to Airflow's XCom database

@dag(
    dag_id='auto_XCom',
    catchup=False
)
def auto_XCom():
    num = task_a()
    task_b(num)
auto_XCom()