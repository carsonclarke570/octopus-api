import argparse
import os
import sys

from flask import Blueprint
from flask import Flask
from flask import g
from flask import request
import redis

from handlers.auth import AuthHandler
from handlers.search import SearchHandler
from handlers.queue import AddToQueueHandler
from handlers.queue import ReadQueueHandler
from handlers.queue import StreamQueueHandler

# API state
api = Blueprint('api', __name__)

@api.route('/', methods=['GET'])
def authorize():
    return AuthHandler().handle()

@api.route('/search', methods=['GET'])
def search():
    return SearchHandler().handle()

@api.route('/queue', methods=['GET', 'POST'])
def queue():
    if request.method == 'GET':
        return ReadQueueHandler().handle()
    if request.method == 'POST':
        return AddToQueueHandler().handle()

@api.route('/stream/queue', methods=['GET'])
def stream_queue():
    return StreamQueueHandler().handle()

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