
class SessionManager:

    SEED = 0

    def __init__(self):
        self.sessions = {}

    def add(self, session):
        SessionManager.SEED = SessionManager.SEED + 1
        self.sessions[SessionManager.SEED] = session
        return SessionManager.SEED

    def get(self, id):
        return self.sessions[id]

    def remove(self, id):
        del self.sessions[id]

    def clear(self):
        self.sessions .clear()