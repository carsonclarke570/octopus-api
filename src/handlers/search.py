from flask import request

from spotify.connection import Connection, ConnectionException
from handlers import APIResponse
from handlers import HandlerException
from handlers.handler import Handler

class SearchHandler(Handler):

    def run(self):
        query = request.args.get('q')
        if query is None:
            raise HandlerException('Missing "q" query parameter')

        params = {
            'q': query,
            'type': 'track'
        }

        try:
            sess = self.session()
            resp = self.connection().get('https://api.spotify.com/v1/search', sess.access_token, params=params)
        except ConnectionException as e:
            return HandlerException(e.message)

        return APIResponse(200, resp)
