
import os
import settings
from flask import Flask, Blueprint
from api.restplus import api
from api.endpoints.temperatures import ns as temperature_namespace

app = Flask(__name__)



def configure_app(flask_app):
    flask_app.config['SERVER_NAME'] = settings.FLASK_SERVER_NAME
    flask_app.config['SWAGGER_UI_DOC_EXPANSION'] = settings.RESTPLUS_SWAGGER_UI_DOC_EXPANSION
    flask_app.config['RESTPLUS_VALIDATE'] = settings.RESTPLUS_VALIDATE
    flask_app.config['RESTPLUS_MASK_SWAGGER'] = settings.RESTPLUS_MASK_SWAGGER
    flask_app.config['ERROR_404_HELP'] = settings.RESTPLUS_ERROR_404_HELP

def initialize_app(flask_app):
    configure_app(flask_app)
    blueprint = Blueprint('', __name__, url_prefix='')
    api.init_app(blueprint)
    api.add_namespace(temperature_namespace)
    flask_app.register_blueprint(blueprint)

def main():
    initialize_app(app)
    app.run(debug=settings.FLASK_DEBUG, port=80, host='localhost')


if __name__ == "__main__":
    main()