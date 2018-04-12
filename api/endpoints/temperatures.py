
import logging

from flask import request
from flask import jsonify
from flask_restplus import Resource, fields
from api.restplus import api
from api.sensors.Temperature import Temperature

log = logging.getLogger(__name__)

ns = api.namespace('api/v1/sensors/temperatures', description='Temperatures sensors')

temperature = api.model('Temperature',{
    'temperature': fields.Integer(readOnly=True, description='The current temperature'),
    'datetime': fields.DateTime(readOnly=True, description='The current time of the measure'),
    'location': {
        'latitude': fields.String(required=True, description='current latitude coordinate'),
        'longitude': fields.String(required=True, description='current longitude coordinate')
    }
})

@ns.route('/')
class Temperatures(Resource):

   @ns.response(200, 'Temperature read')
   @ns.marshal_with(temperature)
   def get(self):
        t = Temperature()
        result = t.read()
        return result