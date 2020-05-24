
class APIResponse:

    def __init__(self, code, content, redirect=None):
        self.resp = {
            'code': code,
            'content': content
        }
        self.redirect = redirect
