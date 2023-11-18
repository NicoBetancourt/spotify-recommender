from repositories.song_repository import SongRepository

class GetAllSongs:

    def __init__(self, song_repository: SongRepository):
        self._song_repository: SongRepository = song_repository

    def execute(self):
        songs = self._song_repository.get_all_songs()
        return songs
