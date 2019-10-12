import json
from flask import Blueprint, request
from services.database.DBConn import database

userDB = database.users
api_1 = Blueprint('api_1', __name__)


@api_1.route("/api_1")
def login():
    username = request.args.get("username")
    password = request.args.get("password")
    return json.dump({'username': username, "password": password})
