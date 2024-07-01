# resources/item.py

from flask_restful import Resource, reqparse

import db

parser = reqparse.RequestParser()
parser.add_argument('ip', type=str, required=True, help='cannot be blank!')
parser.add_argument('executed_at', type=float, required=True, help='cannot be blank!')
parser.add_argument('machine_id', type=int, required=True, help='cannot be blank!')

class MachinePulse(Resource):
    def get(self):
        machine_pulses = db.get_all_machine_pulses()
        return {'machine_pulses': machine_pulses}

    def post(self):
        args = parser.parse_args()
        ip = args['ip']
        executed_at = args['executed_at']
        machine_id = args['machine_id']
        machine_pulse_id = db.execute_machine_pulse(ip, executed_at, machine_id)
        return {'id': machine_pulse_id}, 201
