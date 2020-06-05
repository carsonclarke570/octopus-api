import argparse
import os
import sys

from flask import Flask
from web.routes import APIRouter

# # API state
# api = Blueprint('api', __name__)

# @api.route('/', methods=['GET'])
# def authorize():
#     return AuthHandler().handle()

# @api.route('/search', methods=['GET'])
# def search():
#     return SearchHandler().handle()

# @api.route('/queue', methods=['GET', 'POST'])
# def queue():
#     if request.method == 'GET':
#         return ReadQueueHandler().handle()
#     if request.method == 'POST':
#         return AddToQueueHandler().handle()

# @api.route('/stream/queue', methods=['GET'])
# def stream_queue():
#     return StreamQueueHandler().handle()


def create():
    app = Flask(__name__)

    # Read environement variables
    client_id = os.environ.get('CLIENT_ID')
    secret_id = os.environ.get('CLIENT_SECRET')
    if client_id is None or secret_id is None:
        print("Please provide CLIENT_ID and CLIENT_SECRET environment variables")
        sys.exit(1)

    router = APIRouter(None)
    router.register(app)

    return app

if __name__ == '__main__':
    app = create()
    app.run()