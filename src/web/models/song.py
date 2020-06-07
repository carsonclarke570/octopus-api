from web.models.base import db

class Song(db.Model):
    __tablename__ = 'Song'

    id = db.Column(db.Integer, primary_key=True)
    member_id = db.Column(db.Integer, db.ForeignKey('Member.id'))
    queue_id = db.Column(db.Integer, db.ForeignKey('Queue.id'))

    spotify_id = db.Column(db.String)
    votes = db.Column(db.Integer)

    created_on = db.Column(db.DateTime)
    modified_on = db.Column(db.DateTime)

    def serialize(self):
        return {
            'id': self.id,
            'member_id': self.member_id,
            'queue_id': self.queue_id,

            'spotify_id': self.spotify_id,
            'votes': self.votes,

            'created_on': self.created_on,
            'modified_on': self.modified_on,
        }