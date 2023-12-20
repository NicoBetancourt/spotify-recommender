# # Use cases package
from use_cases.spotify.play_song import PlaySong
from use_cases.spotify.create_token import CreateToken

# Repos
from domain.repositories.spotify_repository import SpotifyRepository
from domain.repositories.token_repository import TokenRepository

_spotify_repo = SpotifyRepository()
_token_repo = TokenRepository()

# Use cases
play_song = PlaySong(_spotify_repo,_token_repo).execute
create_token = CreateToken(_spotify_repo,_token_repo).execute
