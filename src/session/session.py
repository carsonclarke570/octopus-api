import json

from serial.serialize import Serializable

class Session(Serializable):

    def __init__(self, auth_token, refresh_token):
        self.refresh_token = refresh_token
        self.access_token = auth_token
        self.queue = []

    def refresh(self):
        # TODO: Implement
        pass

    def encode(self):
        return json.dumps({
            'refresh_token': self.refresh_token,
            'access_token': self.access_token,
            'queue': self.queue
        });

    @classmethod
    def decode(cls, data):
        data = json.loads(data)
        sess = cls(data['access_token'], data['refresh_token'])
        sess.queue = data['queue']
        return sess
