from spotipy import Spotify
from spotipy import util
from spotipy.oauth2 import SpotifyClientCredentials

class Connection:

    def __init__(self, client_id, client_secret, auth=None):
        self.client_id = client_id
        self.client_secret = client_secret
        self.creds = SpotifyClientCredentials(client_id, client_secret)
        self.api = Spotify(client_credentials_manager=self.creds, auth=auth)
