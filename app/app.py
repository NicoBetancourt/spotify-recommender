from flask_cors import CORS
from flask import Flask
from config import config
from db.client import create_token_table, initialize_database, create_new_table, check_empty_table
from use_cases.song import load_songs

# Routes
from routes.song_routes import song_routes
from routes.admin_routes import admin_routes
from routes.model_routes import model_routes
from routes.spotify_routes import spotify_routes

HTTP_PORT = 5000

app = Flask(__name__)

# Es necesario para poder dejar acceder desde otros puertos
CORS(app)

def page_not_found(error):
    return "<h1>Not found page</h1>"


if __name__ == '__main__':
    app.config.from_object(config['development'])

    # Inicializar database
    initialize_database()
    create_new_table()
    create_token_table()

    # Blueprints
    app.register_blueprint(song_routes, url_prefix='/v1/spotify')
    app.register_blueprint(spotify_routes, url_prefix='/v1/spotify_api')
    app.register_blueprint(admin_routes, url_prefix='/v1/admin')
    app.register_blueprint(model_routes, url_prefix='/v1/model')

    if check_empty_table():
        load_songs()
    # Error handlers
    app.register_error_handler(404, page_not_found)
    app.run(host='0.0.0.0', port=HTTP_PORT, debug=True)