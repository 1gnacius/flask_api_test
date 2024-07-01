# resources/item.py

from datetime import datetime

from flask_restful import Resource, reqparse

import db

parser = reqparse.RequestParser()
parser.add_argument('ip', type=str, required=True, help='cannot be blank!')
parser.add_argument('executed_at', type=str, required=True, help='cannot be blank!')
parser.add_argument('machine_id', type=int, required=True, help='cannot be blank!')

class MachinePulse(Resource):
    def get(self):
        machine_pulses = db.get_all_machine_pulses()
        return {'machine_pulses': machine_pulses}

    def post(self): 
        print("HOLAAAAA")
        args = parser.parse_args()
        ip = args['ip']
        executed_at_str = args['executed_at']
        machine_id = args['machine_id']

        executed_at_dt = datetime.strptime(executed_at_str, '%Y-%m-%dT%H:%M:%S')

        # Obtener el timestamp (float) desde el objeto datetime
        executed_at_timestamp = executed_at_dt.timestamp()

        # Guardar la pulsación de la máquina en la base de datos
        machine_pulse_id = db.execute_machine_pulse(ip, executed_at_timestamp, machine_id)
        
        return {'id': machine_pulse_id}, 201