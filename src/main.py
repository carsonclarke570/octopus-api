import argparse
import os
import sys

from flask import Flask
from web import routes
from web import models


# Required Environment variables
CONFIG = [
    'CLIENT_ID',
    'CLIENT_SECRET',
    'MYSQL_USER',
    'MYSQL_PASS',
    'MYSQL_HOST',
    'MYSQL_DB'
]

def create():

    # Check for environement variables
    failed = False
    for e in CONFIG:
        if os.environ.get(e) is None:
            failed = True
            print(f"Please provide {e} as an environment variable")

    if failed:
        sys.exit(1)

    db_user = os.environ.get('MYSQL_USER')
    db_host = os.environ.get('MYSQL_HOST')
    db_pass = os.environ.get('MYSQL_PASS')
    db_data = os.environ.get('MYSQL_DB')

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{db_user}:{db_pass}@{db_host}/{db_data}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    models.init_app(app)
    routes.init_app(app)

    return app

if __name__ == '__main__':
    app = create()
    app.run()