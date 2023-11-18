from flask import Blueprint
from controller.song_controller import SongController

song_routes = Blueprint("song_routes", __name__)


@song_routes.route('/')
def get_all():
    return SongController.get_all()

@song_routes.route('/<id>')
def get_by_id(id):
    return SongController.get_by_id(id)

@song_routes.route('/', methods=['POST'])
def create():
    return SongController.create()

@song_routes.route('/<id>', methods=['PUT'])
def update(id):
    return SongController.update(id)

@song_routes.route('/<id>', methods=['DELETE'])
def delete(id):
    return SongController.delete(id)

# @song_routes.route("/train-model", methods=["POST"])
# def train_model():
#     return SongController.train_model()
