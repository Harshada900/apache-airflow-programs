from airflow.sdk import Asset, dag, task
#defining asset
sales_asset = Asset("sales_data")
@dag(
    dag_id="load_data",
    catchup=False,
    schedule=None

)
def load_data():

    @task
    def extract()->dict:
        print("Extracting data...")
        return {"sales":50000, "orders":120}

    @task(outlets=[sales_asset])
    def load(data: dict):
        print(f"loading {data['orders']} orders to sales table..")
        print("Done! Asset updated!")
    
    data = extract()
    load(data)

load_data()

@dag(
    dag_id="report_generator",
    catchup=False,
    schedule=[sales_asset]

)
def report_generator():

    @task
    def generate_report():
        print("data received! Generating report...")
        print("Report generated!!")

    generate_report()

report_generator()