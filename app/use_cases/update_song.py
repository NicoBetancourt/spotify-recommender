from domain.entities.song import Song
from domain.repositories.song_repository import SongRepository


class UpdateSong:

    def __init__(self, song_repository: SongRepository):
        self._song_repository: SongRepository = song_repository

    def execute(self, id: int, song_data):
        song = Song(**song_data)
        songInfo = self._song_repository.get_song_by_id(id)
        updatedSong = songInfo.update_song(song)
        self._song_repository.update_song(id, updatedSong)
        return updatedSong
