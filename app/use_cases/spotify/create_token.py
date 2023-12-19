from domain.repositories.spotify_repository import SpotifyRepository

class CreateToken:

    def __init__(self, spotify_repository: SpotifyRepository):
        self.spotify_repository: SpotifyRepository = spotify_repository

    def execute(self):
        result = self.spotify_repository.create_token()
        return result