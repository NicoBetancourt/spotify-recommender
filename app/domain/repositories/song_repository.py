from app.db.driver import psql_driver
from entities.song import Song

COLLECTION_NAME = 'songs';

class SongRepository:

    def __init__(self):
        self.driver = psql_driver()
        self.song = Song()

    def get_song_by_id(self, id):
        song_data = self.driver.get_one(COLLECTION_NAME, id)
        if song_data is not None:
            return self.song.from_dict(song_data)
        else:
            return None

    def get_all_songs(self):
        songs_data = self.driver.get_all(COLLECTION_NAME)
        if songs_data is not None:
            return [self.song.from_dict(song_data) for song_data in songs_data]
        else:
            return []

    def create_song(self, song):
        song_data = song.to_dict()
        return self.driver.create(COLLECTION_NAME, song_data.keys(), song_data.values())

    def update_song(self, song):
        song_data = song.to_dict()
        self.driver.update(
            COLLECTION_NAME,
            song_data.keys(),
            song_data.values(),
            condition=f"id = {song.id}",
        )

    def delete_song(self, id):
        self.driver.delete(COLLECTION_NAME, condition=f"id = {id}")
