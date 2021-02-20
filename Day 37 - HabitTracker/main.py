# see https://pixe.la/v1/users/eugenia/graphs/graph1.html for habit tracker

import requests
from datetime import datetime
import config

# #create user
USERNAME = "eugenia"
TOKEN = config.TOKEN
GRAPH = "graph1"
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# #create graph
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Programming Graph",
    "unit": "hours",
    "type": "int",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# #post a pixel
pix_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH}"

today = datetime.now()
# today = datetime(year=2021, month=2, day=19)

pix_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many hours did you program today? "),
}

response = requests.post(url=pix_endpoint, json=pix_config, headers=headers)
print(response.text)

# #update pixel
update_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPH}/{pix_config["date"]}'

update_config = {
    "quantity": "5"
}

# response = requests.put(url=update_endpoint, json=update_config, headers=headers)
# print(response.text)

# #delete pixel
delete_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPH}/{pix_config["date"]}'

# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)