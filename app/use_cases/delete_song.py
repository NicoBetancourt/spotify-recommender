from repositories.song_repository import SongRepository

class DeleteSong:

    def __init__(self, song_repository: SongRepository):
        self._song_repository: SongRepository = song_repository

    def execute(self, id: int):
        self._song_repository.delete_song(id)
        return "Song deleted"
