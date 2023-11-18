from domain.entities.song import Song
from domain.repositories.song_repository import SongRepository


class UpdateSong:

    def __init__(self, song_repository: SongRepository):
        self._song_repository: SongRepository = song_repository

    def execute(self, id: int, song_data):
        song = Song(**song_data)
        self._song_repository.update_song(id, song)
        return song
