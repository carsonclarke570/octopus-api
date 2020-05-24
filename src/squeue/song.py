import json

from serial.serialize import Serializable

class Song(Serializable):

    def __init__(self, code, id):
        self.code = code
        self.votes = 1
        self.upvoted = [id]
        self.downvoted = []

    def __eq__(self, other):
        if isinstance(other, Song):
            return self.code == other.code
        return False

    def __lt__(self, other):
        if isinstance(other, Song):
            return self.votes < other.votes if self.votes != other.votes else self.code > other.code
        return False

    def __repr__(self):
        return "(" + self.code + ", " + str(self.votes) + ")"

    def upvote(self, id):
        self.votes += 1
        self.upvoted.append(id)

    def downvote(self, id):
        self.votes -= 1
        self.downvoted.append(id)

    def remove_upvoted(self, id):
        self.upvoted.remove(id)
        self.votes -= 1

    def remove_downvoted(self, id):
        self.downvoted.remove(id)
        self.votes += 1

    def encode(self):
        return json.dumps({
            'code': self.code,
            'votes': self.votes,
            'up': self.upvoted,
            'down': self.downvoted
        })

    @classmethod
    def decode(cls, data):
        data = json.loads(data)
        song = cls(data['code'], 0)
        song.upvoted = data['up']
        song.downvoted = data['down']
        return song
