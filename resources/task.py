# resources/task.py

import json
from datetime import datetime

from flask_restful import Resource, reqparse

import db

parser = reqparse.RequestParser()
parser.add_argument('task_name', type=str, required=True, help='cannot be blank!')
parser.add_argument('task_metadata', type=str, required=False, help='cannot be blank!')

def json_type(value):
    try:
        return json.dumps(value)
    except ValueError:
        raise ValueError('Invalid JSON')

class TaskList(Resource):
    def get(self):
        tasks = db.get_all_tasks()
        return {'tasks': tasks}

    # def post(self):
    #     args = parser.parse_args()
    #     task_name = args['task_name']
    #     task_metadata = args['task_metadata']
    #     task_metadata = json_type(task_metadata)
    #     #Guardar la pulsación de la máquina en la base de datos
    #     try:
    #         session_execution_id = db.create_task(task_name,task_metadata)
    #         print((task_metadata))
    #         return {'id': session_execution_id}, 201
    #     except Exception as e:
    #         return {'error': str(e)}, 500