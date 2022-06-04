# ................................. Flight Deal Finder ......................................... #
# Created and modified by N.S.Bhanuprakash on 22-4-2022
# This file helps to find a cheap flight deal between a from_city to desired to_cities
# with a gap of 7-28 days stay between to and from flights.
# This file will need to use the DataManager, FlightSearch, NotificationManager classes
# to achieve the program requirements.

from flight_search import FlightSearch
from datetime import datetime, timedelta
from notification_manager import NotificationManager
from data_manager import DataManager
from pprint import pprint


FROM_DATE = datetime.now() + timedelta(days=1)
TO_DATE = datetime.now() + timedelta(days=6 * 30)
FROM_CITY = "Delhi"
FROM_CITY_IATA = "DEL"
# STOP_OVER_CITY = "Dubai"
# STOP_OVER_IATA = "DXB"
MIN_STAY_DURATION = 7
MAX_STAY_DURATION = 28

flight = FlightSearch()
flight.FLY_FROM = FROM_CITY_IATA
# flight.STOP_OVER = STOP_OVER_IATA
flight.min_stay = MIN_STAY_DURATION
flight.max_stay = MAX_STAY_DURATION
notification = NotificationManager()

# ............ Meta Data used for testing without running whole code ....................... #

# print(flight.flight_details("BOM"))
# print(flight.flight_details(to_city="TYO", from_date=FROM_DATE, to_date=TO_DATE))

# for city_detail in ["PAR", "BOM", "DEL", "BLR"]:
#     city_iata_code = city_detail
#     min_fare_now = flight.flight_details(city_iata_code, FROM_DATE, TO_DATE)["min_fare"]
#     departure = flight.flight_details(city_iata_code, FROM_DATE, TO_DATE)["departure_date"]
#     arrival = flight.flight_details(city_iata_code, FROM_DATE, TO_DATE)["arrival_date"]
#     print(f"{city_iata_code}:{min_fare_now}:{departure}:{arrival}")
# .............................................................................................. #

# sheety = DataManager()
# sheety_data = sheety.prices()
# if sheety_data[0]["iataCode"] == '':
#     sheety.write_sheety(flight_object=flight)
#     sheety_data = sheety.prices()
#
# customer_data = sheety.get_customer_emails()
# customer_mails = [row["email"] for row in customer_data]

# pprint(sheety_data)
# print(customer_mails)

# ............ Meta Data used for testing without running whole code ....................... #

customer_mails = ['nsbprakash95@gmail.com']

sheety_data = [{'city': 'Paris', 'iataCode': 'PAR', 'id': 2, 'lowestPrice': 4468.5},
               {'city': 'Kuala Lumpur', 'iataCode': 'KUL', 'id': 7, 'lowestPrice': 34258.5}]
# {'city': 'Istanbul', 'iataCode': 'IST', 'id': 6, 'lowestPrice': 7861.25},
# {'city': 'Los Angeles', 'iataCode': 'LAX', 'id': 12, 'lowestPrice': 31279.5},
# {'city': 'Berlin', 'iataCode': 'BER', 'id': 3, 'lowestPrice': 3475.5},
# {'city': 'Tokyo', 'iataCode': 'NRT', 'id': 4, 'lowestPrice': 40133.75},
# {'city': 'Sydney', 'iataCode': 'SYD', 'id': 5, 'lowestPrice': 45595.25},
# {'city': 'Montreal', 'iataCode': 'YUL', 'id': 11, 'lowestPrice': 31279.5},
# ]
# {'city': 'New York', 'iataCode': 'NYC', 'id': 8, 'lowestPrice': 19860},
# {'city': 'San Francisco', 'iataCode': 'SFO', 'id': 9, 'lowestPrice': 21515},
# {'city': 'Cape Town', 'iataCode': 'CPT', 'id': 10, 'lowestPrice': 31279.5},
# ]
# ........................................................................................ #

via_city = ""
for city_details in sheety_data:
    to_city = city_details["city"]
    city_iata_code = city_details["iataCode"]
    lowest_price = city_details["lowestPrice"]
    # lowest_price - The price that is affordable for us and is beforehand mentioned in the Google sheet
    try:
        min_fare_now = flight.flight_details(city_iata_code, FROM_DATE, TO_DATE)["min_fare"]
        departure = flight.flight_details(city_iata_code, FROM_DATE, TO_DATE)["departure_date"]
        arrival = flight.flight_details(city_iata_code, FROM_DATE, TO_DATE)["arrival_date"]
        try:
            via_city = flight.flight_details(city_iata_code, FROM_DATE, TO_DATE)["via_city"]
        except KeyError or IndexError:
            print(f"There is a direct flight found for {to_city}")
            # print(f"{city_iata_code}:{min_fare_now}:{departure}:{arrival}")
            pass
        else:
            print(f"No direct flights found for {to_city}")
            print(f"{city_iata_code}:{min_fare_now}:{departure}:{arrival}:via_City:{via_city}")
        if min_fare_now <= lowest_price:
            msg = f"Low price alert 🤑 ! Only ₹{min_fare_now} to travel from {FROM_CITY}-{FROM_CITY_IATA} to " \
                  f"{to_city}-{city_iata_code} from {departure} to {arrival} "
            mail_msg = f"Low price alert 🤑 ! Only ₹{min_fare_now} to travel from {FROM_CITY}-{FROM_CITY_IATA} to " \
                       f"{to_city}-{city_iata_code} from {departure} to {arrival}\n"
            if via_city != '':
                msg = msg + f"via_city: {via_city}"
                mail_msg = mail_msg + f"via_city: {via_city}"
            search_link = flight.flight_details(city_iata_code, FROM_DATE, TO_DATE)["link"]
            notification.sms(sms=msg)
            notification.send_mail(customer_mails=customer_mails, msg=mail_msg, google_link=search_link)
    except TypeError:
        pass
