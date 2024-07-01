# app.py

from flask import Flask
from flask_restful import Api

from resources.item import ItemList

app = Flask(__name__)
api = Api(app)

api.add_resource(ItemList, '/items')

if __name__ == '__main__':
    app.run(debug=True)
