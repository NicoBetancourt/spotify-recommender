from use_cases.model.train_model import TrainModel
from domain.repositories.song_repository import SongRepository
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import MinMaxScaler
import pandas as pd

class RecommenderSongs:

    def __init__(self, song_repository: SongRepository):
        self._song_repository: SongRepository = song_repository
        

    def execute(self, songs_ids, n_songs):
        filter = ""
        songs = self._song_repository.get_all_songs(filter)
        list_of_songs = [song.to_dict() for song in songs]
        df_songs = pd.DataFrame(list_of_songs)

        # Seleccionar las características relevantes para la búsqueda de vecinos cercanos
        features = ['danceability', 'energy', 'key', 'loudness', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo']

        # Normalizar las características
        scaler = MinMaxScaler()
        df_songs[features] = scaler.fit_transform(df_songs[features])

        # Inicializar el modelo NearestNeighbors
        k_neighbors = n_songs  # Número de vecinos cercanos a buscar
        nn_model = NearestNeighbors(n_neighbors=k_neighbors, algorithm='ball_tree')  # Puedes ajustar el algoritmo según tus necesidades

        # Ajustar el modelo a las características de las canciones
        nn_model.fit(df_songs[features])

        list_values = []
        for song_id in songs_ids:
            # chosen_track_id.append(self._song_repository.get_song_by_id(song_id).to_dict())
            chosen_track_id = self._song_repository.get_song_by_id(song_id).to_dict()
            features_values = [chosen_track_id[feature] for feature in features]
            list_values.append(features_values)

        reference_songs_normalized = scaler.transform(pd.DataFrame(list_values))

        # Combinar las características normalizadas de ambas canciones de referencia
        combined_features = reference_songs_normalized.mean(axis=0).tolist()

        # Encontrar los vecinos más cercanos para las canciones de referencia combinadas
        distances, indices = nn_model.kneighbors([combined_features])
        similar_songs = df_songs.loc[indices[0]]

        recommended_songs = []
        for i in range(0,n_songs):
            recommended_songs.append(self._song_repository.get_song_by_id(df_songs.iloc[indices[0][i]]['track_id']).to_dict())

        print(f'Canciones más similares a la canción de referencia:\n{similar_songs}')

        return recommended_songs