from domain.repositories.song_repository import SongRepository

import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics.pairwise import cosine_similarity


class TrainModel:

    def __init__(self, song_repository: SongRepository):
        self._song_repository: SongRepository = song_repository
        self._model = None

    def execute(self):
        filter = ""
        songs = self._song_repository.get_all_songs(filter)
        list_of_songs = [song.to_dict() for song in songs]
        df_songs = pd.DataFrame(list_of_songs)
        #Feature selection
        features = ['danceability', 'energy', 'key', 'loudness', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo']

        # Normalize features
        scaler = MinMaxScaler()
        df_songs[features] = scaler.fit_transform(df_songs[features])

        # Compute cosine similarity between tracks based on selected features
        track_features = df_songs[features]
        track_similarity_matrix = cosine_similarity(track_features, track_features)

        self._model = pd.DataFrame(track_similarity_matrix, index=df_songs['track_id'], columns=df_songs['track_id'])

        return self._model