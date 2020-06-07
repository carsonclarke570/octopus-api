from flask import request

from web.handlers import APIResponse
from web.handlers.handler import Handler

class HealthHandler(Handler):

    def run(self):
        # TO-DO add more health checks (i.e DB)
        statuses = {
            'api': 'ok'
        }
        return APIResponse(200, statuses)