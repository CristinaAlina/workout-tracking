import os
import requests
from datetime import datetime as dt

# Get your app id and api key from https://www.nutritionix.com/business/api
APP_ID = os.environ.get("NUTRIX_APP_ID")
API_KEY = os.environ.get("NUTRIX_API_KEY")

# Create your own Token on https://dashboard.sheety.co/projects/65b50d09ec339004d7c5dc20/auth
SHEETY_BEARER_TOKEN = os.environ.get("SHEETY_BEARER_TOKEN")

nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

user_query = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}
app_parameters = {
    "query": user_query
}

response = requests.post(url=nutritionix_endpoint, json=app_parameters, headers=headers)
nutrix_data = response.json()

exercise_data = nutrix_data["exercises"][0]

# Get your own endpoint after you create a new project on Sheety, connected with Google sheets
add_row_Shitty_endpoint = "https://api.sheety.co/10a134887c3c3d1dd3763fa56c8ef6f6/workoutTracking/workouts"

current_time = dt.today().strftime("%H:%M:%S")
current_date = dt.today().strftime("%d/%m/%Y")

exercise_type = exercise_data["name"].upper()
exercise_duration = exercise_data["duration_min"]
calories_burned = exercise_data["nf_calories"]

# Create your own Bearer (Token) on project Authentication or use another type to authenticate
sheety_header = {
    "Authorization": f"Bearer {SHEETY_BEARER_TOKEN}"
}

# Format row body according to documentation https://sheety.co/docs/requests
body_row = {
    "workout":
        {
            "date": current_date,
            "time": current_time,
            "exercise": exercise_type,
            "duration": exercise_duration,
            "calories": calories_burned
        }
}

sheety_response = requests.post(url=add_row_Shitty_endpoint, json=body_row, headers=sheety_header)
print(sheety_response.text)
