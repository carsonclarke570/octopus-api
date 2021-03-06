import argparse
import os
import sys

from flask import Blueprint
from flask import Flask
from flask import g
from flask import request
import redis

from web.handlers.auth import AuthHandler
from web.handlers.search import SearchHandler
from web.handlers.queue import AddToQueueHandler
from web.handlers.queue import ReadQueueHandler
from web.handlers.queue import StreamQueueHandler

# API state
api = Blueprint('api', __name__)

@api.route('/', methods=['GET'])
def authorize():
    return AuthHandler(args=request.args).handle()

@api.route('/search', methods=['GET'])
def search():
    return SearchHandler(args=request.args).handle()

@api.route('/queue', methods=['GET', 'POST'])
def queue():
    if request.method == 'GET':
        return ReadQueueHandler(
            args=request.args
        ).handle()
    if request.method == 'POST':
        return AddToQueueHandler(
            args=request.args, 
            body=request.get_json()
        ).handle()

@api.route('/stream/queue', methods=['GET'])
def stream_queue():
    return StreamQueueHandler(
        args=request.args
    ).handle()


def create():
    print ("Initializing API")

    app = Flask(__name__)
    app.register_blueprint(api)

    # Read environement variables
    client_id = os.environ.get('CLIENT_ID')
    secret_id = os.environ.get('CLIENT_SECRET')
    if client_id is None or secret_id is None:
        print("Please provide CLIENT_ID and CLIENT_SECRET environment variables")
        sys.exit(1)

    # Initialize redis
    red = redis.Redis(host='redis_db')
    red.set('session_seed', '0')

    return app

if __name__ == '__main__':
    app = create()
    app.run()