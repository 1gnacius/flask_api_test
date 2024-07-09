# app.py

from flask import Flask
from flask_restful import Api

from resources.item import ItemList
from resources.machine_pulse import MachinePulse
from resources.session import SessionExecution
from resources.task import TaskList

app = Flask(__name__)
api = Api(app)

api.add_resource(ItemList, '/items')
api.add_resource(MachinePulse, '/machine_pulse')
api.add_resource(SessionExecution, '/session_execution')
api.add_resource(TaskList, '/tasks')

if __name__ == '__main__':
    app.run(debug=True)
