# app.py

from flask import Flask
from flask_restful import Api

from resources.item import ItemList
from resources.machine_pulse import MachinePulse
from resources.session import SessionConfig, SessionExecution
from resources.sessions import Sessions
from resources.task import Task, TaskList
from resources.task_schedule import TaskSchedule

app = Flask(__name__)
api = Api(app)

api.add_resource(ItemList, '/items')
api.add_resource(MachinePulse, '/machine_pulse')
api.add_resource(SessionExecution, '/session_execution')
api.add_resource(SessionConfig, '/session_config/<int:id>')
api.add_resource(Task, '/task/<int:id>')
api.add_resource(TaskSchedule, '/task_schedule/')
api.add_resource(TaskList, '/tasks')
api.add_resource(Sessions, '/sessions')

if __name__ == '__main__':
    app.run(debug=True)
