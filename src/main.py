import argparse

from flask import Flask
from flask import request
from flask import redirect

from spotify import auth
from spotify.connection import Connection

from session.manager import SessionManager
from session.session import Session


app = Flask(__name__)

manager = SessionManager()
conn = None

@app.route('/', methods=['GET'])
def authorize():
    code = request.args.get('code');
    acc, ref = auth.get_tokens(conn.client_id, conn.client_secret, code)
    session = Session(conn.client_id, conn.client_secret, acc, ref)
    id = manager.add(session)

    return redirect(f"http://localhost:3000/party/{id}", code=302)

@app.route('/p', methods=['GET'])
def playlists():
    sess = manager.get(1)
    tracks = sess.api.current_user_saved_tracks()
    print(tracks)

    return "Hello"


@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('q')
    return client.api.search(query)


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