from utils.dateFormat import DateFormat

class Song():

    def __init__(self, track_id=None, track_name=None, track_artist=None, track_popularity=None, track_album_id=None,
                  track_album_name=None, track_album_release_date=None, playlist_id=None, playlist_name=None, playlist_genre=None,
                  playlist_subgenre=None, danceability=None, energy=None, key=None, loudness=None, mode=None, speechiness=None,
                  acousticness=None, instrumentalness=None, liveness=None, valence=None, tempo=None, duration_ms=None) -> None:
        self.track_id = track_id
        self.track_name = track_name
        self.track_artist = track_artist
        self.track_popularity = track_popularity
        self.track_album_id = track_album_id
        self.track_album_name = track_album_name
        self.track_album_name = track_album_name
        self.track_album_release_date = track_album_release_date
        self.playlist_name = playlist_name
        self.playlist_id = playlist_id
        self.playlist_genre = playlist_genre
        self.playlist_subgenre = playlist_subgenre
        self.danceability = danceability
        self.energy = energy
        self.key = key
        self.loudness = loudness
        self.mode = mode
        self.speechiness = speechiness
        self.acousticness = acousticness
        self.instrumentalness = instrumentalness
        self.liveness = liveness
        self.valence = valence
        self.tempo = tempo
        self.duration_ms = duration_ms

    @classmethod
    def from_dict(cls, data):
        return cls(
            track_id=data.get('track_id'),
            track_name=data.get('track_name'),
            track_artist=data.get('track_artist'),
            track_popularity=data.get('track_popularity'),
            track_album_id=data.get('track_album_id'),
            track_album_name=data.get('track_album_name'),
            track_album_release_date=data.get('track_album_release_date'),
            playlist_name=data.get('playlist_name'),
            playlist_id=data.get('playlist_id'),
            playlist_genre=data.get('playlist_genre'),
            playlist_subgenre=data.get('playlist_subgenre'),
            danceability=data.get('danceability'),
            energy=data.get('energy'),
            key=data.get('key'),
            loudness=data.get('loudness'),
            mode=data.get('mode'),
            speechiness=data.get('speechiness'),
            acousticness=data.get('acousticness'),
            instrumentalness=data.get('instrumentalness'),
            liveness=data.get('liveness'),
            valence=data.get('valence'),
            tempo=data.get('tempo'),
            duration_ms=data.get('duration_ms')
        )

    def to_dict(self):
        return {
            'track_id': self.track_id,
            'track_name': self.track_name,
            'track_artist': self.track_artist,
            'track_popularity': self.track_popularity,
            'track_album_id': self.track_album_id,
            'track_album_name': self.track_album_name,
            'track_album_release_date': self.track_album_release_date,
            'playlist_name': self.playlist_name,
            'playlist_id': self.playlist_id,
            'playlist_genre': self.playlist_genre,
            'playlist_subgenre': self.playlist_subgenre,
            'danceability': self.danceability,
            'energy': self.energy,
            'key': self.key,
            'loudness': self.loudness,
            'mode': self.mode,
            'speechiness': self.speechiness,
            'acousticness': self.acousticness,
            'instrumentalness': self.instrumentalness,
            'liveness': self.liveness,
            'valence': self.valence,
            'tempo': self.tempo,
            'duration_ms': self.duration_ms,
        }
    
    def headers(self):
        return [
            key.lower() for key in self.__dict__.keys()
            if not key.startswith("_")
        ]

    @staticmethod
    def list_to_json(values):
        song = Song()
        song.track_id = values[0]
        song.track_name = values[1]
        song.track_artist = values[2]
        song.track_popularity = values[3]
        song.track_album_id = values[4]
        song.track_album_name = values[5]
        song.track_album_release_date = values[6]
        song.playlist_name = values[7]
        song.playlist_id = values[8]
        song.playlist_genre = values[9]
        song.playlist_subgenre = values[10]
        song.danceability = values[11]
        song.energy = values[12]
        song.key = values[13]
        song.loudness = values[14]
        song.mode = values[15]
        song.speechiness = values[16]
        song.acousticness = values[17]
        song.instrumentalness = values[18]
        song.liveness = values[19]
        song.valence = values[20]
        song.tempo = values[21]
        song.duration_ms = values[22]
        return song
    
    def update_song(self, item):
        # Update attributes with values from 'item' if provided, otherwise retain existing values
        self.track_id = item.track_id if item.track_id else self.track_id
        self.track_name = item.track_name if item.track_name else self.track_name
        self.track_artist = item.track_artist if item.track_artist else self.track_artist
        self.track_popularity = item.track_popularity if item.track_popularity else self.track_popularity
        self.track_album_id = item.track_album_id if item.track_album_id else self.track_album_id
        self.track_album_name = item.track_album_name if item.track_album_name else self.track_album_name
        self.track_album_release_date = item.track_album_release_date if item.track_album_release_date else self.track_album_release_date
        self.playlist_id = item.playlist_id if item.playlist_id else self.playlist_id
        self.playlist_name = item.playlist_name if item.playlist_name else self.playlist_name
        self.playlist_genre = item.playlist_genre if item.playlist_genre else self.playlist_genre
        self.playlist_subgenre = item.playlist_subgenre if item.playlist_subgenre else self.playlist_subgenre
        self.danceability = item.danceability if item.danceability else self.danceability
        self.energy = item.energy if item.energy else self.energy
        self.key = item.key if item.key else self.key
        self.loudness = item.loudness if item.loudness else self.loudness
        self.mode = item.mode if item.mode else self.mode
        self.speechiness = item.speechiness if item.speechiness else self.speechiness
        self.acousticness = item.acousticness if item.acousticness else self.acousticness
        self.instrumentalness = item.instrumentalness if item.instrumentalness else self.instrumentalness
        self.liveness = item.liveness if item.liveness else self.liveness
        self.valence = item.valence if item.valence else self.valence
        self.tempo = item.tempo if item.tempo else self.tempo
        self.duration_ms = item.duration_ms if item.duration_ms else self.duration_ms

        return self

