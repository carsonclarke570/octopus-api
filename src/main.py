import argparse

from flask import Flask

from handlers.auth import AuthHandler
from handlers.search import SearchHandler
from spotify.connection import Connection
from session.manager import SessionManager

app = Flask(__name__)

manager = SessionManager()
conn = None

@app.route('/', methods=['GET'])
def authorize():
    return AuthHandler().handle(conn, manager)

@app.route('/search', methods=['GET'])
def search():
    return SearchHandler().handle(conn, manager)

if __name__ == '__main__':

    # Argument parsing
    parser = argparse.ArgumentParser()
    parser.add_argument('client_id', type=str, help='Enter the Client ID.')
    parser.add_argument('secret_id', type=str, help='Enter the Secret ID.')
    args = parser.parse_args()

    # Create api
    conn = Connection(args.client_id, args.secret_id)

    # Run app
    app.run()