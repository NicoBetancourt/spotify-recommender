from app.controller.base_controller import BaseController
from repositories.song_repository import SongRepository

class SongController(BaseController):

    def __init__(self, song_repository):
        self.song_repository = song_repository

    def get_songs(self):
        return self.song_repository.get_all_songs()

    def get_song_by_id(self, id):
        return self.song_repository.get_song_by_id(id)

    def create_song(self, song_data):
        return self.song_repository.create_song(song_data)

    def update_song(self, id, song_data):
        return self.song_repository.update_song(id, song_data)

    def delete_song(self, id):
        return self.song_repository.delete_song(id)

# Actualizar controladores para llamar los servicios