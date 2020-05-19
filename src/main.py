import argparse

from flask import Flask
from flask import request

from spotify.session import Session

app = Flask(__name__)
session = None

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('q')
    return session.api.search(query)


if __name__ == '__main__':

    # Argument parsing
    parser = argparse.ArgumentParser()
    parser.add_argument('client_id', type=str, help='Enter the Client ID.')
    parser.add_argument('secret_id', type=str, help='Enter the Secret ID.')
    args = parser.parse_args()

    # Create api
    session = Session(args.client_id, args.secret_id)
    results = session.api.search("I Wanna Get Better")
    print(results)

    # Run app
    app.run()