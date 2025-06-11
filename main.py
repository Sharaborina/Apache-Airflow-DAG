import pendulum as pendulum
from airflow import DAG
from airflow.operators.python import PythonOperator
import requests
import pandas as pd
import json

# Загрузка данных о погоде из API OpenWeatherMap и сохранения в файл weather_data.json
def download_weather_data():
    print('starting')
    api_key = '473461bf3491ed06a098c6964e7ad2fe'
    city = 'London'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response = requests.get(url)
    weather_data = response.json()
    with open('weather_data.json', 'w') as f:
        json.dump(weather_data, f)
        print(weather_data)


# Преобразование температуры из Кельвинов в Цельсии и сохранение в файл processed_weather_data.csv
def process_weather_data():
    with open('weather_data.json') as f:
        weather_data = json.load(f)

    main_data = weather_data['main']
    main_data['temp_celsius'] = main_data['temp'] - 273.15  # Преобразование температуры из Кельвинов в Цельсии

    df = pd.DataFrame([main_data])
    df.to_csv('processed_weather_data.csv', index=False)


# Сохранение данных в формате parquet
def save_weather_data():
    df = pd.read_csv('processed_weather_data.csv')
    df.to_parquet('weather.parquet', index=False)


default_args = {
    'owner': 'airflow',
    'start_date': pendulum.today('UTC').add(days=-1),
    'retries': 1,
}

with DAG(
    'weather_data_pipeline_dag',
    default_args=default_args,
    schedule='@daily',
    catchup=False,
) as dag:
    download_task = PythonOperator(
        task_id='download_data',
        python_callable=download_weather_data
    )

    process_task = PythonOperator(
        task_id='process_data',
        python_callable=process_weather_data
    )

    save_task = PythonOperator(
        task_id='save_data',
        python_callable=save_weather_data
    )

    download_task >> process_task >> save_task
