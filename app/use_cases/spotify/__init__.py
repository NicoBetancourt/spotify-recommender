# # Use cases package
from use_cases.spotify.play_song import PlaySong
from use_cases.spotify.create_token import CreateToken

# Repos
from domain.repositories.spotify_repository import SpotifyRepository

_spotify_repo = SpotifyRepository()

# Use cases
play_song = PlaySong(_spotify_repo).execute
create_token = CreateToken(_spotify_repo).execute
