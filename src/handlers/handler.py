from abc import ABC
from abc import abstractmethod
import json
import os

from flask import redirect
from flask import Response
from flask import request
from flask import g

from handlers.response import APIResponse
from session.manager import SessionManager
from spotify.connection import Connection

class HandlerException(Exception):

    def __init__(self, message):
        super.__init__(self)
        self.resp = APIResponse(400, {'message': message}).resp

class Handler(ABC):

    def __init__(self, subscription=None):
        self.manager = SessionManager()
        self.conn = self.connection()
        self.args = request.args

    @abstractmethod
    def run(self):
        pass

    def connection(self):
        if 'connection' not in g:
            client_id = os.environ.get('CLIENT_ID')
            secret_id = os.environ.get('CLIENT_SECRET')
            g.connection = Connection(client_id, secret_id)

        return g.connection

    def session(self):
        id = self.args.get('session')
        if id is None:
            raise HandlerException('Missing "session" query parameter')

        return self.manager.get(id)     


    def handle(self):
        try:
            result = self.run()
        except HandlerException as e:
            return e.resp

        if result.redirect is not None:
            return redirect(result.redirect, code=result.resp['code'])

        return result.resp

class SSEHandler(Handler):

    def __init__(self, subscription):
        super.__init__(self)
        self.sub = subscription

    def handle(self):

        id = self.args.get('session')
        if id is None:
            return HandlerException('Missing "session" query parameter').resp

        def stream():
            ps = self.manager.red.pubsub()
            ps.subscribe(self.sub + id)

            for message in ps.listen():
                if message['type'] == 'message':
                    yield 'data: ' + json.dumps(self.run().resp) + '\n\n'
                    
        resp = Response(stream(),  mimetype="text/event-stream")
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp

class SSEUpdateHandler(Handler):

    def __init__(self, subscription):
        super.__init__(self)
        self.sub = subscription

    def handle(self):
        id = self.args.get('session')
        if id is None:
            return HandlerException('Missing "session" query parameter').resp

        resp = super().handle()
        self.manager.red.publish(self.sub + id, u'')
        self.manager.update(id, s)
        return resp
