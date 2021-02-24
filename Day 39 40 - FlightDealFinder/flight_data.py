#This class is responsible for structuring the flight data.
from data_manager import DataManager
from flight_search import FlightSearch


class FlightData:
    def __init__(self):
        self.flightsearch = FlightSearch()
        self.datamanager = DataManager()
        self.sheety_data = self.datamanager.get_data()

    def data(self, city_codes):
        data = {}
        min_prices = []
        out_date = []
        return_date = []
        for city in city_codes:
            self.flight_info = self.flightsearch.search_flights(city)

            price = self.flight_info["price"]
            min_prices.append(price)

            out = self.flight_info["route"][0]["local_departure"].split("T")[0]
            out_date.append(out)

            back = self.flight_info["route"][1]["local_departure"].split("T")[0]
            return_date.append(back)
        data["prices"] = min_prices
        data["out date"] = out_date
        data["return date"] = return_date
        return data

    def list_cities(self):
        cities = [flight["city"] for flight in self.sheety_data["prices"]]
        return cities

    def orig_prices(self):
        orig_prices = [flight["lowestPrice"] for flight in self.sheety_data["prices"]]
        return orig_prices
