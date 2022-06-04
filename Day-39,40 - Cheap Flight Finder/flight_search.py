# This class is responsible for talking to the Flight Search API.
import requests
import os


class FlightSearch:
    def __init__(self):
        self.TEQUILA_API_KEY = os.getenv("tequila_api_key")   # Hide it in environment variables
            
        # print(os.environ.get("TEQUILA_API_KEY"))
        self.TEQUILA_API_ENDPOINT = "https://tequila-api.kiwi.com"
        self.call_flight_data = "/v2/search"
        self.FLY_FROM = ""
        self.STOP_OVER = ""
        self.num_stops = 0
        self.min_stay = 0
        self.max_stay = 1
        self.header = {
            "apikey": self.TEQUILA_API_KEY,
        }

    def flight_details(self, to_city, from_date, to_date):
        parameters = {
            "fly_from": self.FLY_FROM,
            "fly_to": to_city,
            "date_from": from_date.strftime("%d/%m/%Y"),
            # .strftime("%d/%m/%Y")
            "date_to": to_date.strftime("%d/%m/%Y"),
            # .strftime("%d/%m/%Y")
            "nights_in_dst_from": self.min_stay,
            "nights_in_dst_to": self.max_stay,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "INR",
        }

        response = requests.get(url=f"{self.TEQUILA_API_ENDPOINT}{self.call_flight_data}", params=parameters,
                                headers=self.header)
        response.raise_for_status()
        try:
            # print(response.json())
            # print(to_city)
            flight_data = response.json()["data"][0]
        except IndexError:
            # self.STOP_OVER = "DXB"
            self.num_stops = 1
            parameters["max_stopovers"] = self.num_stops
            # parameters["select_stop_airport"] = self.STOP_OVER
            response = requests.get(url=f"{self.TEQUILA_API_ENDPOINT}{self.call_flight_data}", params=parameters,
                                    headers=self.header)
            response.raise_for_status()
            try:
                flight_data = response.json()["data"][0]
            except IndexError:
                print(f"No flights found for {to_city} even with {self.num_stops} stop_over")
                return None
            # print(f"No flights found for {to_city} ")
            else:
                # print(f"No direct flights found for {to_city}")
                return {
                    "min_fare": flight_data["price"],
                    "departure_date": flight_data["route"][0]["local_departure"].split("T")[0],
                    "arrival_date": flight_data["route"][1]["local_departure"].split("T")[0],
                    "via_city": flight_data["route"][0]["cityTo"],
                    "link": flight_data["deep_link"]
                }
        else:
            # print(f"There is a direct flight found for {to_city}")
            return {
                "min_fare": flight_data["price"],
                "departure_date": flight_data["route"][0]["local_departure"].split("T")[0],
                "arrival_date": flight_data["route"][1]["local_departure"].split("T")[0],
                "link": flight_data["deep_link"]
            }

    def iata_code(self, city):
        code_parmeters = {
            "term": city,
            "location_types": "city"
        }
        locations_endpoint = f"{self.TEQUILA_API_ENDPOINT}/locations/query"
        data = requests.get(url=locations_endpoint, params=code_parmeters, headers=self.header)
        data.raise_for_status()
        data = data.json()
        iata_code = data["locations"][0]['code']
        # print(iata_code)
        return iata_code






