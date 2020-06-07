from flask import request
import requests

from web import crud
from web.handlers import APIResponse
from web.handlers.handler import Handler
from web.models.base import db
from web.models.party import Party
from web.models.queue import Queue
from internal.session.session import Session
from internal.session.manager import SessionManager
from util.errors import APIException

class AuthHandler(Handler):

    def run(self):
        code = self.args.get('code')
        if code is None:
            raise APIException('Missing "code" query parameter!')

        c = self.connection()
        url = 'https://accounts.spotify.com/api/token'
        body = {
            'grant_type': 'authorization_code',
            'code': code,
            'redirect_uri': 'http://localhost:5000/auth/',
            'client_id': c.client_id,
            'client_secret': c.client_secret
        }
        req = requests.post(url, data=body)
        resp = req.json()
    
        if 'access_token' not in resp or 'refresh_token' not in resp:
             raise APIException('Failed to retrieve access and refresh tokens')

        # Create queue
        id = crud.create(Queue())

        # Cretae party
        party = Party(queue_id=id, name='', code='', access_token='', refresh_token='')
        id = crud.create(party)

        db.session.commit()
        
        return APIResponse(302, {}, f"http://localhost:3000/party/{id}")