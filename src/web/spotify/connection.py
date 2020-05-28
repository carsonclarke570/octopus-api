import base64
import requests

class ConnectionException(Exception):

    def __init__(self, message):
        super.__init__(self)
        self.message = message

class Connection:

    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret

    def get(self, endpoint, auth, headers={}, params={}):
        headers['Authorization'] = f'Bearer {auth}'
        r = requests.get(endpoint, headers=headers, params=params)
        try:
            r_json = r.json()
        except ValueError:
            raise ConnectionError(f"Failed to jsonify response: {r.content}")
        
        return r_json

    def post(self, endpoint, auth, headers={}, params={}, body={}):
        headers['Authorization'] = f'Bearer {auth}'
        r = requests.post(endpoint, headers=headers, params=params, data=body)
        try:
            r_json = r.json()
        except ValueError:
            raise ConnectionError(f"Failed to jsonify response: {r.content}")
        
        return r_json
