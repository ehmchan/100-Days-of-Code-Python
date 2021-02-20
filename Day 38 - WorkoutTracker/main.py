import requests
from datetime import datetime
import os

exercise_headers = {
    "x-app-id": os.environ["NT_APP_ID"],
    "x-app-key": os.environ["NT_API_KEY"],
    "x-remote-user-id": "0",
}

GENDER = "female"
WEIGHT = 52.2
HEIGHT = 155
AGE = 25

add_exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

add_exercise_config = {
    "query": input("Tell me which exercises you did: "),
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE,
}

exercise_response = requests.post(url=add_exercise_endpoint, json=add_exercise_config, headers=exercise_headers)
exercises = exercise_response.json()

today = datetime.now()

for exercise in exercises["exercises"]:
    data = {
        "workout": {
            "date": today.strftime("%d/%m/%Y"),
            "time": today.strftime("%I:%M %p"),
            "exercise": (exercise["name"]).title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

    add_row_endpoint = os.environ["SH_endpoint"]
    add_row_response = requests.post(url=add_row_endpoint, json=data, auth=(os.environ["SH_USER"], os.environ["SH_PW"]))
    add_row_response.raise_for_status()
