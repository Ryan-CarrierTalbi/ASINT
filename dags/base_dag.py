from datetime import datetime, timedelta

from airflow.models.dag import DAG
from airflow.operators.python import PythonOperator

with DAG(
    "main_dag",
    default_args={
        "depends_on_past": False,
        "email": ["airflow@example.com"],
        "email_on_failure": False,
        "email_on_retry": False,
        "retries": 1,
        "retry_delay": timedelta(minutes=5),
    },
    description="A simple tutorial DAG",
    schedule=timedelta(days=1),
    start_date=datetime(2021, 1, 1),
    catchup=False,
    tags=["example"],
) as dag:

    def my_py_function(word):
        print(word)
        return 1

    t1 = python_task = PythonOperator(
        task_id="__main__",
        python_callable=my_py_function,
        op_kwargs={"word": "hello world"},
    )