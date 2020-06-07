from web.models.base import db

class Queue(db.Model):
    __tablename__ = 'Queue'

    id = db.Column(db.Integer, primary_key=True)

    created_on = db.Column(db.DateTime)
    modified_on = db.Column(db.DateTime)

    def serialize(self):
        return {
            'id': self.id,

            'created_on': self.created_on,
            'modified_on': self.modified_on,
        }