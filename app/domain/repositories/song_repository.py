from utils.uuii import UniqueId
from db.driver import psql_driver
from domain.entities.song import Song

COLLECTION_NAME = 'songs'

class SongRepository:
    
    def __init__(self):
        self.driver = psql_driver()

    def get_song_by_id(self, id):
        song_data = self.driver.get_one(COLLECTION_NAME, id)
        if song_data is not None:
            return Song.list_to_json(song_data)
        else:
            return None

    def get_all_songs(self,filters):
        songs_data = self.driver.get_all(COLLECTION_NAME, self.filterMap(filters))
        if songs_data is not None:
            return [Song.list_to_json(song_data) for song_data in songs_data]
        else:
            return []

    def create_song(self, song):
        song_data = song.to_dict()
        if song_data['track_id']== None:
            song_data['track_id'] = UniqueId.get_uuid()
        numberSong = self.driver.create(COLLECTION_NAME, song_data.keys(), list(song_data.values()))
        response = {
            "song" : song_data,
            "count": numberSong,
        }
        return response

    def update_song(self, id, song):
        song_data = song.to_dict()
        self.driver.update(
            COLLECTION_NAME,
            song_data.keys(),
            list(song_data.values()),
            condition=f"track_id = '{id}'",
        )
        return song_data

    def delete_song(self, id):
        self.driver.delete(COLLECTION_NAME, condition=f"track_id = '{id}'")

    def filterMap(self, itemArray):
        mapFilter = []
        for item in itemArray:
            if itemArray[item] is not None:
                mapFilter.append(f"{item} LIKE '{itemArray[item]}'")

        condition = ' AND '.join(mapFilter)
        return condition
