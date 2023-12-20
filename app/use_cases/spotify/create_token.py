from datetime import datetime, timedelta
from domain.repositories.spotify_repository import SpotifyRepository
from domain.repositories.token_repository import TokenRepository
from domain.entities.token import Token

class CreateToken:

    def __init__(self, spotify_repository: SpotifyRepository, token_repository: TokenRepository):
        self.spotify_repository: SpotifyRepository = spotify_repository
        self.token_repository: TokenRepository = token_repository

    def execute(self):
        result = self.spotify_repository.create_token()
        access_token = result['access_token']
        expiresIn = datetime.now() + timedelta(seconds=result['expires_in'])
        token = Token(access_token,expiresIn)
        self.token_repository.update_token(token)
        return result