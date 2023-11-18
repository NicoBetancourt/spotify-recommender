from entities.song import Song
from repositories.song_repository import SongRepository

class CreateSong:

    def __init__(self, song_repository: SongRepository):
        self._song_repository: SongRepository = song_repository

    def execute(self, song_data):
        song = Song(**song_data)
        result = self._song_repository.create_song(song)
        return result