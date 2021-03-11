import requests

class Post:
    def __init__(self):
        self.blog_response = requests.get(url=f"https://api.npoint.io/5abcca6f4e39b4955965")
        self.all_posts = self.blog_response.json()