import json
from urllib.parse import quote
from db.request import RequestDriver
from decouple import config

URL_SPOTIFY = 'https://api.spotify.com/v1'
URL_SPOTIFY_ACCOUNT = 'https://accounts.spotify.com/api/token'
SPOTIFY_BASIC_AUTHENTICATION = config('SPOTIFY_BASIC_AUTHENTICATION')

# TOKEN = "BQAVdF6ys_L1lPd5VBuI6YvZsZpzT2UHHTcYyjFsYrhgd0_ZDq3WrLcG274LTUN-owSYdycuw1lrw8jqjuBQVDuqrJIltBNWW5krq9yL3kfSZMu5UbA"

class SpotifyRepository:
    def __init__(self):
        self.http_driver = RequestDriver(URL_SPOTIFY)

    def play_song(self, params,token):
        http_driver = RequestDriver(URL_SPOTIFY)
        name = params['track']
        artist = params['artist']
        path = f"/search"
        params = {
            'q': quote(f'track:{name} artist:{artist}'),
            'type': 'track',
            'limit': 1
        }
        headers = {
            'Authorization': f'Bearer {token}'
        }

        result = http_driver.get(path, params=params, headers=headers)
        if result == None:
            raise Exception("Error de autenticación con Spotify")
            
        return json.loads(result)

    def create_token(self):
        http_driver = RequestDriver(URL_SPOTIFY_ACCOUNT)
        path = ""
        data = {
            "grant_type": "client_credentials"
        }
        headers = {
            "Authorization": f"Basic {SPOTIFY_BASIC_AUTHENTICATION}"
        }
        return http_driver.post(path, data=data, headers=headers)
