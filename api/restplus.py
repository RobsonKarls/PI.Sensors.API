import logging
import traceback
import settings
from flask_restplus import Api, Resource, fields


log = logging.getLogger(__name__)

api = Api(version='1.0', title='Sensors API',
          description='Sensor reading RESTFul API')


@api.errorhandler
def default_error_handler(e):
    message = 'An unhandled exception occurred.'
    log.exception(message)

    if not settings.FLASK_DEBUG:
        return {'message': message}, 500