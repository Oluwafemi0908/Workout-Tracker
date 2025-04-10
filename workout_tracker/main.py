import requests
from datetime import datetime
import os
#
os.environ['APP_ID'] = "42c263e9"
os.environ["APP_API"] = "4bfc0b1b5ada2676bb6e0495e77fb26d"
os.environ["SHEET_ENDPOINT"] = "https://api.sheety.co/df3797fff716dd2337a79ceb1838a4b2/myWorkouts/workouts"
os.environ["TOKEN"] = "adsghjjrtyw434678gfxcvbnmdw45dds"
APP_ID = os.getenv("APP_ID")
APP_API = os.getenv("APP_API")
nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = os.getenv("SHEET_ENDPOINT")
bearer_headers = {
    "Authorization": f"Bearer {os.getenv("TOKEN")}"
}
date = datetime.now().date().strftime("%d/%m/%Y")
time = datetime.now().time().strftime("%H:%M:%S")
parameter = {
    'query': input('Kindly input the exercise here:')
}


headers = {
    'x-app-id': APP_ID,
    'x-app-key': APP_API
}

response = requests.post(url=nutritionix_endpoint, json=parameter, headers=headers)
data = response.json()
tasks = data['exercises']
for task in tasks:
    sheet_parameter = {
        'workout': {
            'date': date,
            'time': time,
            'exercise': task['name'].title(),
            'duration': task['duration_min'],
            'calories': task['nf_calories']

        }
    }
    sheety_response = requests.post(url=sheety_endpoint, json=sheet_parameter, headers=bearer_headers)
    print(sheety_response)
