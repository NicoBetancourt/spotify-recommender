from flask import Blueprint
from controller.spotify_controller import SpotifyController

spotify_routes = Blueprint("spotify_routes", __name__)


@spotify_routes.route('/search', methods=['POST'])
def get_track():
    return SpotifyController.play_song()

@spotify_routes.route('/token')
def create_token():
    return SpotifyController.create_token()
