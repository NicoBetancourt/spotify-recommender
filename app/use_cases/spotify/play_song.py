from datetime import datetime
from domain.repositories.spotify_repository import SpotifyRepository
from domain.repositories.token_repository import TokenRepository
from domain.entities.token import Token
from datetime import datetime, timedelta
class PlaySong:

    def __init__(self, spotify_repository: SpotifyRepository, token_repository: TokenRepository):
        self._spotify_repository: SpotifyRepository = spotify_repository
        self.token_repository: TokenRepository = token_repository

    def execute(self,params):

        acces_token = self.token_repository.get_token()

        if acces_token.expiresIn < datetime.now() or not acces_token :
            token = self._spotify_repository.create_token()
            access_token = token['access_token']
            expiresIn = datetime.now() + timedelta(seconds=token['expires_in'])
            token = Token(access_token,expiresIn)
            self.token_repository.update_token(token)
            acces_token = self.token_repository.get_token()

        result = self._spotify_repository.play_song(params,acces_token.tokenKey)

        info_song = result['tracks']['items'][0]['preview_url']

        if info_song is None:
            info_song = "Not found"
        
        preview_url = {
            "preview_url": info_song
        }
        return preview_url