from controller.base_controller import BaseController
from flask import jsonify, request

# import use cases
from use_cases.model import recommend_songs, train_model2

class ModelController(BaseController):

    @staticmethod
    def train_model():
        try:
            train_model2()
            return 'Model trained'
        except Exception as ex:
                    return jsonify({'Error message': str(ex)}), 500
        
    @staticmethod
    def recommend_songs():
        try:
            json = request.json
            id = json['id']
            n_songs = json['n_songs']
            songs = recommend_songs(id, n_songs)

            return {
                "count": songs,
                "song": len(songs),
            }
        
        except Exception as ex:
                    return jsonify({'Error message': str(ex)}), 500
        