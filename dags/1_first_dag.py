from airflow.sdk import dag, task
import pendulum # for dates
'''
@dag(
    dag_id="first_dag"
    start_date=pendulum.datetime(2026, 1, 1, tz="UTC"),
    schedule="@daily",
    catchup=False,
    tags=["beginner","example"]
)'''
@dag(
    dag_id="first_dag"
)
def first_dag():
    @task
    def extract():
        print("Step: Extracting...")
        return {"name":"Rahul", "score":98} #returns data to next task
    @task
    def transform(data):
        print("Step 2: Transforming...")
        data["grade"] = "A"
        return data
    @task
    def load(data):
        print(f"Step 3 Loading Data - {data}")
        print("Done! Data saved to warehouse")

    raw_data = extract()
    cleaned_data = transform(raw_data)
    load(cleaned_data)  # this is an implicit chain -> Linear !

first_dag()

