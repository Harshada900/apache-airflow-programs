#wait for a file to appear in a folder

from airflow.sensors.filesystem import FileSensor

wait_for_file = FileSensor(
    task_id = "wait_for_file",
    filepath = "/home/harshada/data/sales.csv",
    poke_interval = 30,           # check every 3- seconds
    timeout = 3600,
    mode = "rescheduled"        #efficient waiting check -> not found -> dead -> 30 seconds late check again and so on..
     
)