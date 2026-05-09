from airflow.sdk import dag, task
import pendulum

@dag(
    dag_id="branching_dag",
    catchup=False,
    schedule=None
)
def branching_dag():
    @task.branch
    def check_condition():
        day = pendulum.now().day_of_week

        if day<5:
            return "weekday_task"
        else:
            return "weekend_task"
    @task
    def weekend_task():
        print("Its weekday! running full ETL ")

    @task
    def weekday_task():
        print("Its weekday! running light summary!")

    @task(trigger_rule="none_failed_min_one_success")
    def end_task():
        print("pipeline done regardless of which branch/task executed")

    #chain
    decider= check_condition()
    end = end_task()
    decider >> [weekend_task(), weekday_task()] >> end

branching_dag()