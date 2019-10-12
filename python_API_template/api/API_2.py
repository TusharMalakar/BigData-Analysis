import json
from flask import Blueprint, request
from services.database.DBConn import database

userDB = database.users
api_2 = Blueprint('api_2', __name__)


@api_2.route("/api_2")
def login():
    username = request.args.get("username")
    password = request.args.get("password")
    return json.dump({'username': username, "password": password})
