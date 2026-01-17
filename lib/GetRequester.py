# lib/GetRequester.py
import requests
import json

class GetRequester:
    def __init__(self, url):
        """
        Initialize the class with a URL
        """
        self.url = url

    def get_response_body(self):
        """
        Send a GET request to the URL and return the body of the response
        """
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        """
        Send a GET request using get_response_body and return JSON data
        """
        response_body = self.get_response_body()
        # Convert the response body (bytes/str) to Python object (list/dict)
        return json.loads(response_body)
