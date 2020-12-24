import requests

addr = "http://127.0.0.1:5000/api"

class Api(object):
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.session = requests.session()

    def auth(self):
        self.session.post(f"{addr}/login/{self.username}/{self.password}")
