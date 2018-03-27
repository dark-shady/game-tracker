import json
import requests
from urllib.parse import urljoin

class Opendota:
    def __init__(self):
        self.BASE_URL = "https://api.opendota.com/api/"

    def make_request(self, api_url):
        try:
            r = requests.get(urljoin(self.BASE_URL, api_url))
            r.raise_for_status()
        except requests.exceptions.HTTPError as err:
            print (err)

        return json.loads(r.text)
