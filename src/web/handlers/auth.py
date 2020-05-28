from flask import request

from web.handlers import APIResponse
from web.handlers import HandlerException
from web.handlers.handler import Handler
from web.spotify import auth
from internal.session.session import Session
from internal.session.manager import SessionManager

class AuthHandler(Handler):

    def run(self):
        code = self.args.get('code');
        if code is None:
            raise HandlerException('Missing "code" query parameter!')

        c = self.conn
        acc, ref = auth.get_tokens(c.client_id, c.client_secret, code)
        if acc is None or ref is None:
            raise HandlerException('Failed to retrieve access and refresh tokens')

        id = self.manager.add(Session(acc, ref))
        
        return APIResponse(302, {}, f"http://localhost:3000/party/{id}")