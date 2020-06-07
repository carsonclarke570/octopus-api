from flask_restx  import Namespace, Resource

from web.handlers.health import HealthHandler

api = Namespace('health', description='Querying for various API services health')

@api.route('/')
class APIHealth(Resource):

    @api.doc('check_alive')
    def get(self):
        return HealthHandler().handle()