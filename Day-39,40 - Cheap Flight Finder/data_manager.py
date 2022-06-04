# This class is responsible for talking to the Google Sheet.
import requests


class DataManager:
    def __init__(self):
        self.SHEETY_API_ENDPOINT = "https://api.sheety.co/d940733305c9a7b9c1afb5377504782b/flightDeals/prices"
        # Hide it in environment variables
        self.SHEETY_HEADER = {
            "Authorization": "Bearer tomandjerry"
        }  # Hide it in environment variables
        self.response = requests.get(url=self.SHEETY_API_ENDPOINT, headers=self.SHEETY_HEADER)
        self.response.raise_for_status()
        self.sheety_data = self.response.json()
        self.customer_data = []

    def prices(self):
        return self.sheety_data["prices"]

    def write_sheety(self, flight_object):
        sheety_data = self.prices()
        for row in sheety_data:
            city_name = row["city"]
            city_id = row["id"]
            iata_code = flight_object.iata_code(city_name)
            sheety_put_request = f"{self.SHEETY_API_ENDPOINT}/{city_id}"
            body = {
                "price": {
                    "iataCode": iata_code
                }
            }
            response = requests.put(url=sheety_put_request, json=body, headers=self.SHEETY_HEADER)
            response.raise_for_status()
            # print(response.json())
            self.response = requests.get(url=self.SHEETY_API_ENDPOINT, headers=self.SHEETY_HEADER)
            self.response.raise_for_status()
            self.sheety_data = self.response.json()

    def get_customer_emails(self):
        customers_endpoint = "https://api.sheety.co/d940733305c9a7b9c1afb5377504782b/flightDeals/users"
        mail_data = requests.get(url=customers_endpoint, headers=self.SHEETY_HEADER)
        data = mail_data.json()
        # print(data)
        self.customer_data = data["users"]
        return self.customer_data
