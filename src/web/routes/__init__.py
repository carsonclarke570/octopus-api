""" routes - route package """

from flask_restplus import Api

from web.routes.auth import api as auth_api
from web.routes.health import api as health_api

class APIRouter:

    ROUTES = [
        { 'route': auth_api, 'enable': False },
        { 'route': health_api, 'enable': True }
    ]

    def __init__(self, db):
        self.db = db
        self.api = Api(
            title='Octopus API',
            version='1.0',
            description='Octopus API'
        )

    def register(self, app):
        for route in APIRouter.ROUTES:
            if route['enable']:
                self.api.add_namespace(route['route'])

        self.api.init_app(app)
