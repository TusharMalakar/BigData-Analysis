import os
from flask import Flask
from flask_cors import CORS

from api.API_1 import api_1
from api.API_2 import api_2
from api.AuthorizationAPI import auth_api


app = Flask(__name__)
CORS(app)
app.register_blueprint(api_1, url_prefix='/one') #All endpoints in API_1.py are prefixed with the /one route.
app.register_blueprint(api_2, url_prefix='/two') #All endpoints in API_2.py are prefixed with the /two route.
app.register_blueprint(auth_api, url_prefix='/auth') #All endpoints in Authorization.py are prefixed with the /auth route.


# Root
@app.route("/", methods=['GET'])
def helloWorld():
    return "Welcome Tiny URL Services."


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, threaded=True)
