from flask import request

from handlers.handler import Handler, HandlerException
from handlers.response import APIResponse
from spotify import auth
from session.session import Session

class AuthHandler(Handler):

    def run(self, connection, manager):
        code = request.args.get('code');
        if code is None:
            raise HandlerException('Missing "code" query parameter!')

        acc, ref = auth.get_tokens(connection.client_id, connection.client_secret, code)
        if acc is None or ref is None:
            raise HandlerException('Failed to retrieve access and refresh tokens')

        id = manager.add(Session(connection.client_id, connection.client_secret, acc, ref))
        
        return APIResponse(302, {}, f"http://localhost:3000/party/{id}")