"""
    this api will distribute who should use which api
"""
import json
from flask import Blueprint, request
from services.database.DBConn import database

userDB = database.users
auth_api = Blueprint('auth_api', __name__)


@auth_api.route("/login")
def login():
    username = request.args.get("username")
    password = request.args.get("password")
    return json.dump({'username': username, "password": password})
