# Use cases package
from use_cases.model.recommender_songs import RecommenderSongs
# Repos
from domain.repositories.song_repository import SongRepository

_info_repo = SongRepository()

# Use cases
recommend_songs = RecommenderSongs(_info_repo).execute

