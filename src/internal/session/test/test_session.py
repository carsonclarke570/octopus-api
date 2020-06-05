import pytest

from internal.session.session import Session

class TestSession():

    def test_encode(self):
        sess = Session('auth', 'ref')
        dump = sess.encode()
        assert dump == '{"refresh_token": "ref", "access_token": "auth", "queue": "[]"}'

    def test_decode(self):
        sess = Session.decode('{"refresh_token": "ref", "access_token": "auth", "queue": "[]"}')
        assert sess.access_token == 'auth'
        assert sess.refresh_token == 'ref'
        assert sess.queue.queue == []
