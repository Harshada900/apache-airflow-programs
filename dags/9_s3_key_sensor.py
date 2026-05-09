from airflow.providers.amazon.aws.sensors.s3 import S3KeySensor

wait_for_s3_file = S3KeySensor(
    task_id="wait_for_s3_file",
    bucket_name="my-data-bucket",       #which s3 bucket
    bucket_key="data/sales.csv",        #whcih file to wait for
    aws_conn_id="my_aws_conn",          #AWS connection
    poke_interval=30,                   
    timeout=3600,
    mode="reschedule"
)