Weather Data Pipeline using Apache Airflow
This project is an Airflow DAG that automates the process of fetching weather data from the OpenWeatherMap API, converting temperature values, and saving the processed data for further use.

📦 Features
Fetches current weather data for London.

Converts temperature from Kelvin to Celsius.

Saves raw data in weather_data.json.

Saves processed data in processed_weather_data.csv.

🛠️ Technologies Used
- Python
- Apache Airflow
- Pandas
- Requests
- JSON

🧠 Workflow Overview
Download Weather Data
Calls the OpenWeatherMap API and saves the response as weather_data.json.

Process Weather Data
Converts temperature to Celsius and saves selected fields to processed_weather_data.csv.

📂 File Structure
bash
Copy
Edit
main.py                  # Contains the DAG definition and Python functions
weather_data.json        # Raw weather data from the API
processed_weather_data.csv # Processed weather data with temperature in Celsius

🚀 Getting Started
Prerequisites
Python 3.7+
Airflow
A valid OpenWeatherMap API key

Installation
Clone the repository:

git clone https://github.com/your-username/weather-dag.git
cd weather-dag

Install dependencies:

pip install apache-airflow pandas requests
Set up Airflow and add the main.py to your DAGs folder.

🗓️ Scheduling
This DAG is scheduled to run daily at midnight UTC.

schedule_interval='0 0 * * *'

🔐 API Key
Replace the placeholder API key in main.py:

api_key = 'your_actual_api_key'
⚠️ Never expose your real API keys in public repositories.

📬 Output
weather_data.json — Full response from the OpenWeatherMap API.

processed_weather_data.csv — Extracted and converted weather data.

📄 License
MIT License
