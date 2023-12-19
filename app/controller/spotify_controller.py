from controller.base_controller import BaseController
from flask import jsonify, request

# import use cases
from use_cases.spotify import create_token, play_song

class SpotifyController(BaseController):

    @staticmethod
    def play_song():
        try:
            json = request.json
            response = play_song(dict(json))
            print("play spong response: ", response)
            return response
        except Exception as ex:
                    return jsonify({'Error message': str(ex)}), 500
        
    @staticmethod
    def create_token():
        try:
            return create_token()
        except Exception as ex:
                    return jsonify({'Error message': str(ex)}), 500
        