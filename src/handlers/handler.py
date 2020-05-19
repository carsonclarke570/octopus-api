from abc import ABC, abstractmethod
from flask import redirect

from handlers.response import APIResponse

class HandlerException(Exception):

    def __init__(self, message):
        Exception.__init__(self)
        self.resp = APIResponse(400, {'message': message}).resp

class Handler(ABC):

    @abstractmethod
    def run(self, connection, manager):
        pass

    def handle(self, connection, manager):
        try:
            result = self.run(connection, manager)
        except HandlerException as e:
            return e.resp

        if result.redirect is not None:
            return redirect(result.redirect, code=result.resp['code'])

        return result.resp
