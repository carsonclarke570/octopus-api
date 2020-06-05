from flask import request
import time

from web.handlers import APIResponse
from web.handlers import HandlerException
from web.handlers.handler import Handler
from web.handlers.handler import SSEHandler
from web.handlers.handler import SSEUpdateHandler
from internal.squeue.song import Song

class ReadQueueHandler(Handler):

    def run(self):
        queue = self.session()
        
        songs = []
        for s in queue.queue.queue:
            songs.append(s.code)

        print(songs)

        return APIResponse(200, {"songs": songs})


class StreamQueueHandler(SSEHandler):

    def __init__(self, args):
        SSEHandler.__init__(self, 'queue', args=args)

    def run(self):
        queue = self.session()
        
        songs = []
        for s in queue.queue.queue:
            songs.append(s.code)

        print(songs)

        return APIResponse(200, {"songs": songs})

class AddToQueueHandler(SSEUpdateHandler):

    def __init__(self, args, body):
        SSEUpdateHandler.__init__(self, 'queue', args=args, body=body)

    def run(self):
        id = self.args.get('session')
        if id is None:
            raise HandlerException('Missing "session" query parameter')

        song = self.body.get('song')
        if song is None:
            raise HandlerException('Missing parameter "song" in body')

        sid = self.body.get('id')
        if sid is None:
            raise HandlerException('Missing parameter "id" in body')
            
        song = Song(song, sid)

        s = self.session()
        s.queue.queue.append(song)
        self.manager.update(id, s)

        return APIResponse(200, {"status": "success"})


