#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from flight_search import FlightSearch
from flight_data import FlightData
from data_manager import DataManager
from notification_manager import NotificationManager

sheety_data = DataManager()
search = FlightSearch()
notif = NotificationManager()
flight_data = FlightData()

# search for IATA codes
cities = flight_data.list_cities()
city_codes = search.get_codes(cities)

# # write city codes into google sheet
# sheety_data.put_data(city_codes)

# find cheapest flights for all cities
data = flight_data.data(city_codes)

min_prices = data["prices"]
out_date = data["out date"]
return_date = data["return date"]

# find original price of flights
orig_prices = flight_data.orig_prices()

# if min price < orig price send alert
alert_city_num = [num for num in range(len(min_prices)) if min_prices[num] < orig_prices[num]]
for num in alert_city_num:
    flight_city = cities[num]
    flight_code = city_codes[num]
    cost = min_prices[num]
    out = out_date[num]
    ret = return_date[num]
    notif.send_alert(cost, flight_city, flight_code, out, ret)
