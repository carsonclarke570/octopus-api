from web.models.base import db

from web.models.song import Song

class Queue(db.Model):
    __tablename__ = 'Queue'

    id = db.Column(db.Integer, primary_key=True)
    songs = db.relationship('Song', backref='Queue', lazy=True)

    created_on = db.Column(db.DateTime)
    modified_on = db.Column(db.DateTime)

    def serialize(self):
        return {
            'id': self.id,
            'songs': list(map(lambda x : x.serialize(), self.songs)),

            'created_on': self.created_on,
            'modified_on': self.modified_on,
        }