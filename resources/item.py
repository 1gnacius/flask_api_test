# resources/item.py

from flask_restful import Resource, reqparse

import db

parser = reqparse.RequestParser()
parser.add_argument('name', type=str, required=True, help='Name cannot be blank!')
parser.add_argument('description', type=str, required=True, help='Description cannot be blank!')

class ItemList(Resource):
    def get(self):
        items = db.get_all_items()
        return {'items': items}

    def post(self):
        args = parser.parse_args()
        name = args['name']
        description = args['description']
        item_id = db.create_item(name, description)
        return {'id': item_id}, 201
