from flask_restx  import Namespace, Resource
from flask import request

from web.handlers.crud import CreateHandler
from web.handlers.crud import ReadHandler
from web.handlers.crud import UpdateHandler
from web.handlers.crud import DeleteHandler
from web.handlers.crud import FilterHandler
from web.models.queue import Queue

api = Namespace('queue', description='Queue related functions')

@api.route('/')
class QueueRoute1(Resource):

    @api.doc('check_alive')
    def get(self):
        return FilterHandler(Queue).handle()

    def post(self):
        return CreateHandler(Queue).handle()

@api.route('/<int:id>/')
class QueueRoute2(Resource):

    def get(self, id):
        return ReadHandler(Queue).handle()

    def delete(self, id):
        return DeleteHandler(Queue).handle()