import requests


class Blogs:

    def __init__(self):
        self.blog_url = " https://api.npoint.io/c790b4d5cab58020d391"

    def get_posts(self):
        response = requests.get(self.blog_url)
        return response.json()