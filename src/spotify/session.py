from spotipy import Spotify
from spotipy.oauth2 import SpotifyClientCredentials

class Session:

    def __init__(self, client_id, client_secret):
        self.creds = SpotifyClientCredentials(client_id, client_secret)
        self.api = Spotify(client_credentials_manager=self.creds)