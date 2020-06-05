from flask_restplus import Namespace, Resource

api = Namespace('health', description='Enpoints for querying API health')

@api.route('/')
class APIHealth(Resource):

    @api.doc('check_alive')
    def get(self):
        return "Healthy"