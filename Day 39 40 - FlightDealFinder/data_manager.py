# This class is responsible for talking to the Google Sheet.
import requests
import os

sheety_endpoint = os.environ["SH_endpoint"]


class DataManager:
    def __init__(self):
        self.endpoint = sheety_endpoint

    def get_data(self):
        self.get_data_response = requests.get(url=self.endpoint, auth=(os.environ["SH_USER"], os.environ["SH_PW"]))
        self.get_flight_data = self.get_data_response.json()
        return self.get_flight_data

    def put_data(self, city_codes):
        for num in range(len(city_codes)):
            code_data = {
                "price": {
                    "iataCode": city_codes[num]
                }
            }
            # self.put_data_response = requests.put(url=f"{self.endpoint}/{num+2}", json=code_data, auth=(os.environ["SH_USER"], os.environ["SH_PW"]))
            # self.put_data_response.raise_for_status()
