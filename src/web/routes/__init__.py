""" routes - route package """

from flask_restx import Api

from web.routes.auth import api as auth_api
from web.routes.health import api as health_api
from web.routes.queue import api as queue_api

ROUTES = [
    { 'route': auth_api, 'enable': True },
    { 'route': health_api, 'enable': True },
    { 'route': queue_api, 'enable': True },
]

def init_app(app):
    api = Api(
        title='Octopus API',
        version='1.0',
        description='Octopus API',
        doc='/doc/'
    )

    for route in ROUTES:
        if route['enable']:
            api.add_namespace(route['route'])

    api.init_app(app)
