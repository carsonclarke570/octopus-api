from datetime import datetime 

from web.models.base import db

def create(model):
    model.id = None
    model.created_on = datetime.now()
    model.modified_on = datetime.now()

    db.session.add(model)
    db.session.flush()
    db.session.commit()

    return model.id

def read(model_type, id):
    return model_type.query.get(id)

def update():
    pass

def delete(model_type, id):
    db.session.query(model_type).filter(model_type.id == id).delete()
    db.session.commit()

def filter(model_type, **kwargs):
    results = model_type.query.filter_by(**kwargs).all()
    if results is None:
        return []

    return list(map(lambda x: x.serialize(), results))
