import requests

class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()

    def get(self, endpoint, headers=None, params=None):
        url = f"{self.base_url}{endpoint}"
        return self.session.get(url, headers=headers, params=params)

    def post(self, endpoint, headers=None, data=None, json=None):
        url = f"{self.base_url}{endpoint}"
        return self.session.post(url, headers=headers, data=data, json=json)

    def put(self, endpoint, headers=None, data=None, json=None):
        url = f"{self.base_url}{endpoint}"
        return self.session.put(url, headers=headers, data=data, json=json)

    def delete(self, endpoint, headers=None):
        url = f"{self.base_url}{endpoint}"
        return self.session.delete(url, headers=headers)
