from flask_restx import Namespace, Resource

from web.handlers.auth import AuthHandler

api = Namespace('auth', description='Authentication endpoints')

@api.route('/')
class Auth(Resource):

    @api.doc('auth')
    def get(self):
        return AuthHandler().handle()