# Use cases package
from use_cases.song.create_song import CreateSong
from use_cases.song.get_all_songs import GetAllSongs
from use_cases.song.get_song import GetSong
from use_cases.song.update_song import UpdateSong
from use_cases.song.delete_song import DeleteSong
from use_cases.song.load_songs import LoadSongs

# Repos
from domain.repositories.song_repository import SongRepository

_info_repo = SongRepository()

# Use cases
create_song = CreateSong(_info_repo).execute
get_all_songs = GetAllSongs(_info_repo).execute
get_song_by_id = GetSong(_info_repo).execute
update_song = UpdateSong(_info_repo).execute
delete_song = DeleteSong(_info_repo).execute
load_songs = LoadSongs(_info_repo).execute

