from flask_restful import reqparse
from flask.ext.restful import Resource
from db_model import addService, getServiceList
from service_resource import parse
from bson.json_util import dumps
from service_parsers import ServiceListParser

class ServiceListResource(Resource):

    def get(self):
        args = ServiceListParser.parseGetParameters()
        if 'number' in args:
            number = args['number']
        else:
            number = None
        if 'offset' in args:
            offset = args['offset']
        else:
            offset = None
        serviceList = getServiceList(number, offset)
        return serviceList

    def post(self):
        listAgrs = ServiceListParser.parsePostParameters()
        result = addService(listAgrs.get('name'), listAgrs.get('logSize'), listAgrs.get('ownerId'))
        if result is None:
            return  "Service already exists", 400
        return dumps(result, ensure_ascii=False).encode('utf8')
        
def parser():
    parser = reqparse.RequestParser()
    parser.add_argument('number', type=int, default=None)
    parser.add_argument('offset', type=int, default=None)
    args = parser.parse_args()
    return args