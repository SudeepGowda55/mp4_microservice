from flask import Flask, request
import jwt, datetime, os

wapp = Flask(__name__)
wapp.config['MYSQL_HOST'] = os.environ.get("MYSQL_HOST")

@wapp.route('/')
def hello():
    return "hello"

@wapp.route('/login', methods=["POST"])
def login():
    auth = request.authorization
    if not auth:
        return "missing credentials", 401
    else:
        return "Ok"

if __name__ == "__main__":
    wapp.run(host="127.0.0.1", port=3033, debug=True)
