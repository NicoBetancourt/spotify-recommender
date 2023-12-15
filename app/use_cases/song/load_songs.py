from domain.repositories.song_repository import SongRepository
from domain.entities.song import Song
import pandas as pd
from tqdm import tqdm

database = 'app/resources/spotify_songs.csv'

class LoadSongs:

    def __init__(self, song_repository: SongRepository):
        self._song_repository: SongRepository = song_repository

    def execute(self):
        table = pd.read_csv(database)
        table.drop_duplicates(subset=['track_id'], inplace=True)
        list_of_songs = table.to_dict(orient='records')
        progress_bar = tqdm(total=len(list_of_songs), desc='Cargando base de datos:')
        count = 0
        for item in list_of_songs:
            song = Song(**item)
            try:
                self._song_repository.create_song(song)
                count += 1
            except:
                print('Número de registros cargados: ', count)
            progress_bar.update(1)
        print('Tabla de datos cargada exitosamente')
