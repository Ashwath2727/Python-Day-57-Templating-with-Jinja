import requests

class AgeCalculator:

    def __init__(self, name):
        print("Initializing AgeCalculator")
        self.age_url = "https://api.agify.io"
        self.name = name

    def get_age(self):
        params = {
            "name": self.name,
        }
        response = requests.get(self.age_url, params=params)
        return response.json()["age"]
