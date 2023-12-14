# Use cases package
from use_cases.model.recommender_songs import RecommenderSongs
from use_cases.model.train_model import TrainModel
# Repos
from domain.repositories.song_repository import SongRepository

_info_repo = SongRepository()

# Use cases
train_model2 = TrainModel(_info_repo).execute
recommend_songs = RecommenderSongs(_info_repo).execute

