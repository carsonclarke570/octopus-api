from spotify.connection import Connection

class Session(Connection):

    def __init__(self, client_id, client_secret, auth_token, refresh_token):
        super().__init__(client_id, client_secret, auth_token)
        self.refresh_token = refresh_token
        self.access_token = auth_token

    def refresh(self):
        pass