from airflow.sdk import dag, task

@dag(dag_id="my_dag")
def my_dag():
    @task.python
    def task_a():
        print("this is task a")
    
    @task.python
    def task_b():
        print("this is task b")
    
    @task.python
    def task_c():
        print("this is task c")
    
    @task.python
    def task_d():
        print("this is task d")

    #instantiate
    task_a = task_a()
    task_b = task_b()
    task_c = task_c()
    task_d = task_d()

    #dependency operator - task_ a runs first 
    task_a>> task_b
    #reverse dependency operator - still task a runs firts
    task_b<< task_a
    #types of task dependencies
    #1 linear - one after another
    task_a>> task_b >> task_c >> task_d

    #parallel - multiple tasks at same time

    #task_a >> [task_b, task_c] >> task_d  # task b and c runs parallel

    # Fan out - one splits into many 
    #task_a >> [task_b, task_c, task_d]

    #fan in - many merge into one
    #[task_a, task_b, task_c] >> task_d

#since we are not passing any data we are using >>

my_dag()