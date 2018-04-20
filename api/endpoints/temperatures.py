
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
    'latitude': fields.String(required=True, description='current latitude coordinate'),
    'longitude': fields.String(required=True, description='current longitude coordinate'),
    'time_utc': fields.DateTime(readOnly=True, description='The current GPS UTC time'),
    'altitude': fields.String(required=True, description='current GPS altitude'),
    'speeding': fields.String(required=True, description='current GPS speeding'),
    'sound': fields.String(required=True, description='sound level'),
    'humiture': fields.String(required=True, description='humidity level'),
    'flame': fields.String(required=True, description='Flame detection')
})

@ns.route('/')
class Temperatures(Resource):

   @ns.response(200, 'Temperature read')
   @ns.marshal_with(temperature)
   def get(self):
        t = Temperature()
        result = t.read()
        return result