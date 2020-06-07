""" models - Models module """

from web.models.base import db

def init_app(app):
    db.init_app(app)


