# from repositories.song_repository import SongRepository


def get_all_songs(song_repository):
    songs = song_repository.get_all_songs()
    return songs