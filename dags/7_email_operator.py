from airflow.operators.email import EmailOperator
from airflow.sdk import dag

@dag(
    dag_id="email_op_dag",
    catchup=False,
    default_args = {
        "email_on_failure": False,
        "email_on_retry": False
}
)
def email_op_dag():
    ob = EmailOperator(
        task_id= "send_email",
        to="harshadabhoir441@gmail.com",
        subject="Daily Report Ready!",
        html_content = "<h1> Your Daily Report is Ready !! </h1>"
    )
email_op_dag()      # u need to set up SMTP connection I havent set so it will failed!