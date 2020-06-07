import pytest
import flask

from web.handlers import APIResponse
from web.handlers.health import HealthHandler

class TestHealthHandler():

    def test_run(self):
        with flask.Flask(__name__).test_request_context('/test'):
            handler = HealthHandler()
            resp = handler.run()
            assert isinstance(resp, APIResponse)
            assert resp.resp['code'] == 200
            assert resp.resp['content'] == {'api': 'ok'}