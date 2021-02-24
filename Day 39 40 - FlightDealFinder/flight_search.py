import requests
import os
from datetime import datetime, timedelta

API_KEY = os.environ["flight_api"]
endpoint = "https://tequila-api.kiwi.com/"

flight_headers = {
    "apikey": API_KEY
}


class FlightSearch:
    def __init__(self):
        self.TQ_API_KEY = API_KEY
        self.TQ_endpoint = endpoint

    def get_codes(self, cities):
        self.codes = []
        for city in cities:
            flight_config = {
                "term": city,
            }
            location_response = requests.get(url=f"{self.TQ_endpoint}locations/query", params=flight_config,
                                             headers=flight_headers)
            location_response.raise_for_status()
            location = location_response.json()
            self.codes.append(location["locations"][0]["code"])
        return self.codes

    def search_flights(self, city):
        tomorrow = datetime.today() + timedelta(days=1)
        six_months = datetime.today() + timedelta(days=180)
        search_config = {
            "fly_from": "LON",
            "fly_to": city,
            "date_from": tomorrow.strftime("%d/%m/%Y"),
            "date_to": six_months.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "max_stopovers": "0",
            "curr": "GBP"
        }
        search_response = requests.get(url=f"{endpoint}v2/search", params=search_config, headers=flight_headers)
        self.searches = search_response.json()["data"][0]
        return self.searches
