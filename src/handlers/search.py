from flask import request

from handlers.handler import Handler, HandlerException
from handlers.response import APIResponse

class SearchHandler(Handler):

    def run(self, connection, manager):
        query = request.args.get('q')
        if query is None:
            raise HandlerException('Missing "q" query parameter')

        return APIResponse(200, connection.api.search(query))