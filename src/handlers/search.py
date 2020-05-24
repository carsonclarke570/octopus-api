from flask import request

from spotify.connection import Connection, ConnectionException
from handlers.handler import Handler, HandlerException
from handlers.response import APIResponse

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
