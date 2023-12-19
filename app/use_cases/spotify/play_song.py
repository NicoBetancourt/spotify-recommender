from domain.repositories.spotify_repository import SpotifyRepository

class PlaySong:

    def __init__(self, spotify_repository: SpotifyRepository):
        self._spotify_repository: SpotifyRepository = spotify_repository

    def execute(self,params):
        result = self._spotify_repository.play_song(params)

        info_song = result['tracks']['items'][0]['preview_url']

        if info_song is None:
            info_song = "Not found"
        
        preview_url = {
            "preview_url": info_song
        }
        print(preview_url)
        return preview_url