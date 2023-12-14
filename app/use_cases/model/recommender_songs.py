from use_cases.model.train_model import TrainModel
from domain.repositories.song_repository import SongRepository
import pandas as pd
from domain.repositories.song_repository import SongRepository

_info_repo = SongRepository()

class RecommenderSongs:

    def __init__(self, song_repository: SongRepository):
        self._song_repository: SongRepository = song_repository
        

    def execute(self, song_id, n_songs):
        filter = ""
        songs = self._song_repository.get_all_songs(filter)
        list_of_songs = [song.to_dict() for song in songs]
        df_songs = pd.DataFrame(list_of_songs)
        train_model2 = TrainModel(_info_repo)
        train_model2.execute()

        #Feature selection
        chosen_song_index = df_songs[df_songs['track_id'] == song_id].index[0]
        similarity_scores = self._model.iloc[chosen_song_index]
        similar_songs = similarity_scores.sort_values(ascending=False)
        top_similar_songs = similar_songs.iloc[1:n_songs+1]
        top_similar_song_ids = top_similar_songs.index.tolist()
        top_similar_songs_details = df_songs[df_songs['track_id'].isin(top_similar_song_ids)]

        return top_similar_songs_details