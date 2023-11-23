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
    
def initialize_database():
    try:
        connection = psycopg2.connect(
            host=config('PGSQL_HOST'),
            user=config('PGSQL_USER'),
            password=config('PGSQL_PASSWORD'),
            dbname='postgres',
            port=config('PGSQL_PORT')
        )

        connection.autocommit = True
        cur = connection.cursor()

        cur.execute(f"SELECT 1 FROM pg_database WHERE datname = %s", (config('PGSQL_DATABASE'),))
        result = cur.fetchone()
        if result is None:
            cur.execute(f'CREATE DATABASE "{config("PGSQL_DATABASE")}" WITH OWNER = {config("PGSQL_USER")}')

        cur.close()
        connection.close()

    except DatabaseError as ex:
        raise ex

def create_new_table():

    create_table = f"""
                CREATE TABLE IF NOT EXISTS {table_name} (
                    track_id CHAR(50) PRIMARY KEY,
                    track_name VARCHAR(255),
                    track_artist VARCHAR(255),
                    track_popularity SMALLINT,
                    track_album_id VARCHAR(50),
                    track_album_name VARCHAR(255),
                    track_album_release_date VARCHAR(50),
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

def check_empty_table():
    try:
        connection = get_connection()
        cur = connection.cursor()

        # Verificar si la tabla está vacía
        cur.execute(f"SELECT 1 FROM {table_name} LIMIT 1")
        result = cur.fetchone()

        return result is None

    except DatabaseError as ex:
        print(f"Error al verificar si la tabla está vacía: {ex}")
        return False

    finally:
        cur.close()
        connection.close()