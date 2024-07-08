# resources/item.py

import json
from datetime import datetime

from flask_restful import Resource, reqparse

import db

parser = reqparse.RequestParser()
parser.add_argument('ip', type=str, required=True, help='cannot be blank!')
parser.add_argument('executed_at', type=str, required=True, help='cannot be blank!')
parser.add_argument('machine_id', type=int, required=True, help='cannot be blank!')
parser.add_argument('execution_log', type=str, required=False, help='cannot be blank!')

def json_type(value):
    try:
        return json.dumps(value)
    except ValueError:
        raise ValueError('Invalid JSON')

class SessionExecution(Resource):

    def post(self):
        args = parser.parse_args()
        ip = args['ip']
        executed_at = args['executed_at']
        machine_id = args['machine_id']
        execution_log = args['execution_log']
        print(execution_log)
        print(type(execution_log))
        execution_log = json_type(execution_log)
        print(type(execution_log))
        #Guardar la pulsación de la máquina en la base de datos
        try:
            session_execution_id = db.execute_session(ip, executed_at, machine_id, execution_log)
            print((ip, executed_at, machine_id, execution_log))
            return {'id': session_execution_id}, 201
        except Exception as e:
            return {'error': str(e)}, 500