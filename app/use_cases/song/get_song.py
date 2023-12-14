from domain.repositories.song_repository import SongRepository


class GetSong:

    def __init__(self, song_repository: SongRepository):
        self._song_repository: SongRepository = song_repository

    def execute(self, id: int):
        song = self._song_repository.get_song_by_id(id)
        return song
