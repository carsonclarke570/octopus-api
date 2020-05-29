from unittest import mock
import os

import flask
import pytest

from internal.session.session import Session
from web.handlers import APIResponse
from web.handlers.handler import Handler


class TestHandler(Handler):

    def run(self):
        return APIResponse(200, {"songs": ["I Wanna", "Get Better"]})


class TestHandlerClass():

    def setup_class(self):
        os.environ['CLIENT_ID'] = "ID"
        os.environ['CLIENT_SECRET'] = "SECRET"
        self.handler = TestHandler(
            args={'session': 1}
        )
        self.handler.manager = mock.MagicMock()
        self.handler.manager.get = mock.MagicMock(return_value=Session('auth', 'refr'))

    def teardown_class(self):
        del os.environ['CLIENT_ID']
        del os.environ['CLIENT_SECRET']

    def test_connection(self):
        with flask.Flask(__name__).test_request_context('/test'):
            conn = self.handler.connection()
            assert conn.client_id == 'ID'
            assert conn.client_secret == 'SECRET'

    def test_session(self):
        sess = self.handler.session()
        assert sess.refresh_token == 'refr'
        assert sess.access_token == 'auth'
