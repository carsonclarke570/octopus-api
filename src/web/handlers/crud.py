from flask import request
from flask import jsonify
import time

from web import crud
from web.handlers import APIResponse
from web.handlers.handler import Handler
from util.errors import APIException

class CreateHandler(Handler):

    def __init__(self, model_type):
        Handler.__init__(self)
        self.model_type = model_type

    def run(self):
        resp = {
            'status': 'Sucessfully created new model',
            'id': -1
        }
        try:
            model = self.model_type(**request.json)
            resp['id'] = crud.create(model)
        except Exception as e:
            raise APIException(str(e))

        return APIResponse(200, resp)


class ReadHandler(Handler):
    
    def __init__(self, model_type):
        Handler.__init__(self)
        self.model_type = model_type

    def run(self):
        id = request.view_args.get('id')
        
        if id is None:
            raise APIException("The path is missing paramater 'id'")
        
        try:
            model = crud.read(self.model_type, id)
        except Exception as e:
            raise APIException(str(e))

        return APIResponse(200, model.serialize())

class UpdateHandler(Handler):
    pass

class DeleteHandler(Handler):

    def __init__(self, model_type):
        Handler.__init__(self)
        self.model_type = model_type

    def run(self):
        id = request.view_args.get('id')
        if id is None:
            raise APIException("The path is missing paramater 'id'")
        
        try:
            crud.delete(self.model_type, int(id))
        except Exception as e:
            raise APIException(str(e))

        return APIResponse(200, 'Sucessfully deleted model')

class FilterHandler(Handler):
    
    def __init__(self, model_type):
        Handler.__init__(self)
        self.model_type = model_type

    def run(self):
        try:
            model_list = crud.filter(self.model_type, **request.json)
        except Exception as e:
            raise APIException(str(e))

        return APIResponse(200, model_list)
