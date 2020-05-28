""" handlers - API Handlers """

class APIResponse:

    def __init__(self, code, content, redirect=None):
        self.resp = {
            'code': code,
            'content': content
        }
        self.redirect = redirect

class HandlerException(Exception):

    def __init__(self, message):
        Exception.__init__(self)
        self.resp = APIResponse(400, {'message': message}).resp

