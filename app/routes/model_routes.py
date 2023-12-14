from flask import Blueprint
from controller.model_controller import ModelController

model_routes = Blueprint("model_routes", __name__)


@model_routes.route('/train/')
def train():
    return ModelController.train_model()

@model_routes.route('/recommend/', methods=['POST'])
def recommend():
    return ModelController.recommend_songs()
