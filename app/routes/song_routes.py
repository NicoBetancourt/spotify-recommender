from flask import Blueprint, request, jsonify
from entities.song import Song
from repositories.song_repository import SongRepository

song_routes = Blueprint("song_routes", __name__)


@song_routes.route("/", methods=["GET"])
def get_songs():
    song_repository = SongRepository()
    songs = song_repository.get_all_songs()
    return jsonify(songs)


@song_routes.route("/<id>", methods=["GET"])
def get_song_by_id(id):
    song_repository = SongRepository()
    song = song_repository.get_song_by_id(id)
    return jsonify(song)


@song_routes.route("/", methods=["POST"])
def create_song():
    song_data = request.get_json()
    song = Song(**song_data)
    song_repository = SongRepository()
    song_repository.create_song(song)
    return jsonify(song)


@song_routes.route("/<id>", methods=["PUT"])
def update_song(id):
    song_data = request.get_json()
    song = Song(**song_data)
    song_repository = SongRepository()
    song_repository.update_song(song)
    return jsonify(song)


@song_routes.route("/<id>", methods=["DELETE"])
def delete_song(id):
    song_repository = SongRepository()
    song_repository.delete_song(id)
    return jsonify({"message": "Song deleted"})


@song_routes.route("/train-model", methods=["POST"])
def train_model():
    song_repository = SongRepository()
    song_repository.delete_song()
    return jsonify({"message": "Song deleted"})

# Actualizar rutas para llamar los controladores