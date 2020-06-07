from web.models.base import db

class Party(db.Model):
    __tablename__ = 'Party'

    id = db.Column(db.Integer, primary_key=True)
    queue_id = db.Column(db.Integer, db.ForeignKey('Queue.id'))
    host_id = db.Column(db.Integer, db.ForeignKey('Host.id'))

    name = db.Column(db.String(255))
    code = db.Column(db.String(5), unique=True)
    access_token = db.Column(db.String(255))
    refresh_token = db.Column(db.String(255))

    created_on = db.Column(db.DateTime)
    modified_on = db.Column(db.DateTime)

    def serialize(self):
        return {
            'id': self.id,
            'queue_id': self.queue_id,

            'name': self.name,
            'code': self.code,
            'access_token': self.access_token,
            'refresh_token': self.refresh_token,

            'created_on': self.created_on,
            'modified_on': self.modified_on,
        }
