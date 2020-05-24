from flask import request
import time

from handlers.handler import Handler
from handlers.handler import HandlerException
from handlers.handler import SSEHandler
from handlers.handler import SSEUpdateHandler
from handlers.response import APIResponse

class ReadQueueHandler(Handler):

    def __init__(self):
        super.__init__(self)

    def run(self):
        s = self.session()
        return APIResponse(200, {"songs": s.queue})


class StreamQueueHandler(SSEHandler):

    def __init__(self):
        super.__init__(self, 'queue')

    def run(self):
        s = self.session()
        return APIResponse(200, {"songs": s.queue})

class AddToQueueHandler(SSEUpdateHandler):

    def __init__(self):
        SSEUpdateHandler.__init__(self, 'queue')

    def run(self):
        id = self.args.get('session')
        if id is None:
            raise HandlerException('Missing "session" query parameter')

        song = self.args.get('song')
        if song is None:
            raise HandlerException('Missing "song" query parameter')

        s = self.session()
        s.queue.append(song)

        return APIResponse(200, {"status": "success"})


