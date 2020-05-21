class Song:

    def __init__(self, code, votes, ip):
        self.code = code
        self.votes = votes
        self.upvoted = [ip]
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

    def upvote(self, ip):
        self.votes += 1
        self.upvoted.append(ip)

    def downvote(self, ip):
        self.votes -= 1
        self.downvoted.append(ip)

    def remove_upvoted(self, ip):
        self.upvoted.remove(ip)
        self.votes -= 1

    def remove_downvoted(self, ip):
        self.downvoted.remove(ip)
        self.votes += 1

    def get_upvoted(self):
        return self.upvoted

    def get_downvoted(self):
        return self.downvoted
