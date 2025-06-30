from celery import Celery
import json
import psycopg2

app = Celery('tasks', broker='redis://redis:6379/0')

DB_CONFIG = {
    "dbname": "iot_data",
    "user": "user",
    "password": "password",
    "host": "postgres"
}

@app.task
def process_sensor_data(message):
    data = json.loads(message)
    prediction = data["temperature"] * 0.1  # Mock prediction
    data["prediction"] = prediction

    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                "INSERT INTO sensor_data (sensor_id, temperature, humidity, prediction) VALUES (%s, %s, %s, %s)",
                (data["sensor_id"], data["temperature"], data["humidity"], data["prediction"])
            )
            conn.commit()
    print(f"Processed and saved: {data}")
