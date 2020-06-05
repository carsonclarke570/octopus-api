from unittest import mock
import json
import os

import flask
import pytest

from internal.session.session import Session
from util.errors import APIException
from web.handlers import APIResponse
from web.handlers.handler import Handler


class ExHandler(Handler):

    def run(self):
        if 'fail' in self.args:
            raise APIException('Failed')
        else:
            if 'redirect' in self.args:
                return APIResponse(302, {}, "myredirect")
            else:
                return APIResponse(200, {"songs": ["I Wanna", "Get Better"]})


class TestHandlerClass():

    def setup_method(self):
        os.environ['CLIENT_ID'] = "ID"
        os.environ['CLIENT_SECRET'] = "SECRET"
        self.handler = ExHandler(
            args={'session': 1}
        )
        self.handler.manager = mock.MagicMock()
        self.handler.manager.get = mock.MagicMock(return_value=Session('auth', 'refr'))

    def teardown_method(self):
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

    def test_handle_success(self):
        with flask.Flask(__name__).test_request_context('/test'):
            resp = self.handler.handle()
            data = json.loads(resp.data)

            assert resp.headers['Access-Control-Allow-Origin'] == '*'
            assert data['code'] == 200
            assert data['content'] == {"songs": ["I Wanna", "Get Better"]}

    def test_handle_redirect(self):
        with flask.Flask(__name__).test_request_context('/test'):
            self.handler.args['redirect'] = "fsfd"
            resp = self.handler.handle()

            assert resp.status_code == 302

    def test_handle_exception(self):
        with flask.Flask(__name__).test_request_context('/test'):
            self.handler.args['fail'] = "fsfd"
            resp = self.handler.handle()
            data = json.loads(resp.data)

            assert resp.status_code == 400
            assert data['code'] == 400
            assert data['content'] == {'error': 'Failed'}

