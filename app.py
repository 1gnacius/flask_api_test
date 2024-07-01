# app.py

from flask import Flask
from flask_restful import Api

from resources.item import ItemList
from resources.machine_pulse import MachinePulse

app = Flask(__name__)
api = Api(app)

api.add_resource(ItemList, '/items')
api.add_resource(MachinePulse, '/machine_pulse')

if __name__ == '__main__':
    app.run(debug=True)
