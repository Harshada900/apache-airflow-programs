from airflow.sdk import dag, task, get_current_context

@dag(
    dag_id='manual_XCom',
    catchup=False
)
def manual_XCom():
    @task
    def task_a():
        context = get_current_context()
        ti = context['ti']                       #getting task info from kwarghs is discouraged, now get_current_context() is the new standard way
        ti.xcom_push(key="return_result", value=67)    
    @task
    def task_b():
        context = get_current_context()
        ti = context['ti']          # ti represents the current task i.e task b here

        num = ti.xcom_pull(
            task_ids="task_a",
            key = "return_result"
        )
        print(f"Value is {num}")
    push = task_a()
    pull = task_b()

    push >> pull
manual_XCom()