from domain.entities import Song
from db.driver import PsqlDriver

class SongRepository:

    def __init__(self):
        self.driver = PsqlDriver()

    def get_song_by_id(self, id):
        song_data = self.driver.get_one("songs", id)
        if song_data is not None:
            return Song.from_dict(song_data)
        else:
            return None

    def get_all_songs(self):
        songs_data = self.driver.get_all("songs")
        if songs_data is not None:
            return [Song.from_dict(song_data) for song_data in songs_data]
        else:
            return []

    def create_song(self, song):
        song_data = song.to_dict()
        self.driver.create("songs", song_data.keys(), song_data.values())

    def update_song(self, song):
        song_data = song.to_dict()
        self.driver.update(
            "songs",
            song_data.keys(),
            song_data.values(),
            condition=f"id = {song.id}",
        )

    def delete_song(self, id):
        self.driver.delete("songs", condition=f"id = {id}")
