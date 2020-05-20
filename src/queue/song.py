class Song:

    def __init__(self, code, votes, ip):
        self.code = code
        self.votes = votes
        self.ip_voted = [ip]

    def __lt__(self, other):
        return self.votes < other.votes if self.votes != other.votes else self.code < other.code

    def __repr__(self):
        return self.code
