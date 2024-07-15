# resources/item.py

import json
from datetime import datetime

from flask_restful import Resource, reqparse

import db


def json_type(value):
    try:
        return json.dumps(value)
    except ValueError:
        raise ValueError('Invalid JSON')

class Sessions(Resource):
    def get(self, id):
        sessions = db.get_all_sessions(id)
        return {'sessions': sessions}