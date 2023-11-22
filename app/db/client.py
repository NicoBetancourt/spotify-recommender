import psycopg2
from psycopg2 import DatabaseError
from decouple import config

table_name = config('TABLE_NAME')

def get_connection():
    try:
        # Conéctate a la base de datos
        return psycopg2.connect(
            host=config('PGSQL_HOST'),
            user=config('PGSQL_USER'),
            password=config('PGSQL_PASSWORD'),
            database=config('PGSQL_DATABASE'),
            port=config('PGSQL_PORT')
        )
    except DatabaseError as ex:
        raise ex

def create_new_table():

    print('Crea la base de datos {} si no existe'.format(table_name))
    create_table = f"""
                CREATE TABLE IF NOT EXISTS {table_name} (
                    track_id CHAR(10) PRIMARY KEY,
                    track_name VARCHAR(255),
                    track_artist VARCHAR(255),
                    track_popularity SMALLINT,
                    track_album_id VARCHAR(50),
                    track_album_name VARCHAR(255),
                    track_album_release_date DATE,
                    playlist_name VARCHAR(255),
                    playlist_id VARCHAR(50),
                    playlist_genre VARCHAR(255),
                    playlist_subgenre VARCHAR(255),
                    danceability FLOAT,
                    energy FLOAT,
                    key SMALLINT,
                    loudness FLOAT,
                    mode SMALLINT,
                    speechiness FLOAT,
                    acousticness FLOAT,
                    instrumentalness FLOAT,
                    liveness FLOAT,
                    valence FLOAT,
                    tempo FLOAT,
                    duration_ms INTEGER
                )
                """

    connection = get_connection()
    cur = connection.cursor()
    cur.execute(create_table)
    connection.commit()