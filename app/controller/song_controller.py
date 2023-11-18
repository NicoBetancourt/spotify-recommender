from controller.base_controller import BaseController
from flask import jsonify, request

# import use cases
from use_cases import create_song, get_song_by_id, get_all_songs, update_song, delete_song

class SongController(BaseController):

    @staticmethod
    def create():
        try:
            json = request.json
            data = create_song(json)

            response = {
                "count": data,
            }
            return response
        except Exception as ex:
                    return jsonify({'Error message': str(ex)}), 500
        
    @staticmethod
    def update(id):
        try:
            json = request.json
            data = update_song(id, json)

            response = {
                "id": id,
                "info": data.to_dict(),
            }

            return response
        except Exception as ex:
                    return jsonify({'Error message': str(ex)}), 500
        
    @staticmethod
    def delete(id):
        try:
            id = delete_song(id)

            response = {
                "id": id,
            }

            return response
        except Exception as ex:
                    return jsonify({'Error message': str(ex)}), 500
        
    @staticmethod
    def get_all():
        try:
            data = get_all_songs()

            response = {
                "count": len(data),
                "info": [song.to_dict() for song in data],
            }

            return response
        except Exception as ex:
                    return jsonify({'Error message': str(ex)}), 500
        
    @staticmethod
    def get_by_id(id):
        try:
            data = get_song_by_id(id)

            response = {
                "id": id,
                "info": data.to_dict(),
            }

            return response
        except Exception as ex:
                    return jsonify({'Error message': str(ex)}), 500