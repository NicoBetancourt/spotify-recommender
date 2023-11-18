# Use cases package
from use_cases.create_song import CreateSong
from use_cases.get_all_songs import GetAllSongs
from use_cases.get_song import GetSong
from use_cases.update_song import UpdateSong
from use_cases.delete_song import DeleteSong

# Repos
from domain.repositories.song_repository import SongRepository

_info_repo = SongRepository()

# Use cases
create_song = CreateSong(_info_repo).execute
get_all_songs = GetAllSongs(_info_repo).execute
get_song_by_id = GetSong(_info_repo).execute
update_song = UpdateSong(_info_repo).execute
delete_song = DeleteSong(_info_repo).execute

