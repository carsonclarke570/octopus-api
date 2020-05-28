from flask import g
import redis

from internal.session.session import Session

class SessionManager:

    def __init__(self):
        self.red = self.get_redis()

    def get_redis(self):
        if 'red' not in g:
            g.red = redis.Redis(host='redis_db')

        return g.red

    def add(self, session):
        id = int(self.red.get('session_seed')) + 1
        self.red.set('s' + str(id), session.encode())
        self.red.set('session_seed', id)
        return id

    def get(self, id):
        data = self.red.get('s' + str(id))
        return Session.decode(data)

    def update(self, id, session):
        data = session.encode()
        self.red.set('s' + str(id), data)

    def remove(self, id):
        self.red.delete('s' + str(id))
