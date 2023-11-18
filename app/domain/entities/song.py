from utils.dateFormat import DateFormat

class Song():

    def __init__(self, track_id, track_name=None, track_artist=None, track_popularity=None, track_poputrack_album_idlarity=None,
                  track_album_name=None, track_album_release_date=None, playlist_id=None, playlist_name=None, playlist_genre=None,
                  playlist_subgenre=None, danceability=None, energy=None, key=None, loudness=None, mode=None, speechiness=None,
                  acousticness=None, instrumentalness=None, liveness=None, valence=None, tempo=None, duration_ms=None) -> None:
        self.track_id = track_id
        self.track_name = track_name
        self.track_artist = track_artist
        self.track_popularity = track_popularity
        self.track_album_id = track_poputrack_album_idlarity
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
            track_id=data['track_id'],
            track_name=data.get('track_name'),
            track_artist=data.get('track_artist'),
            track_popularity=data.get('track_popularity'),
            track_poputrack_album_idlarity=data.get('track_album_id'),
            track_album_name=data.get('track_album_name'),
            track_album_release_date=DateFormat.convert_date_from_str(data.get('track_album_release_date')),
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
            'track_album_release_date': DateFormat.convert_data(self.track_album_release_date),
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
