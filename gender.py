import requests

class Gender:

    def __init__(self, name):
        print("Initializing Gender")
        self.gender_url = "https://api.genderize.io"
        self.name = name


    def get_gender(self):
        params = {
            "name": self.name,
        }
        response = requests.get(self.gender_url, params=params)
        # print(response.json())
        return response.json()["gender"]