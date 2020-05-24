from flask import request
import time

from handlers.handler import SSEHandler, HandlerException
from handlers.response import APIResponse

class ReadQueueHandler(SSEHandler):

    def __init__(self):
        self.count = 0
        self.timer = time.perf_counter()

    def run(self, connection, manager):
        self.count += 1
        return APIResponse(200, {"yeet": self.count})

    def check(self, connection, manager):
        now = time.perf_counter()
        if  now - self.timer > 5.0:
            self.timer = now
            return True

        return False