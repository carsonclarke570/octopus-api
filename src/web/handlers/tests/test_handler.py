from unittest import mock
import os

from flask import g
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
        self.handler = TestHandler()

    def teardown_class(self):
        del os.environ['CLIENT_ID']
        del os.environ['CLIENT_SECRET']

    def setup_method(self):
        self.handler.args = {
            'session': 1
        }
        self.manager = mock.MagicMock()
        self.manager.get = mock.MagicMock(return_value=Session("auth", "refr"))

    def test_connection(self):
        del g['connection']
        conn = self.handler.connection()
        assert conn.client_id == 'ID'
        assert conn.client_secret == 'SECRET'

    def test_session(self):
        sess = self.handler.session()
        assert sess.refresh_token == 'refr'
        assert sess.access_token == 'auth'
        