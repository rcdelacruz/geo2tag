from flask_restful import reqparse
from flask.ext.restful import Resource
from channels_list_parsers import ChannelsListResourceParser
from db_model import getChannelsList
class ChannelsListResource(Resource):
    def get(self, serviceName):
        parserResult = ChannelsListResourceParser.parseGetParameters()
        print parserResult.get('substring', ''), parserResult.get('number', -1), parserResult.get('offset', -1)
        return getChannelsList(serviceName, parserResult.get('substring', ''), parserResult.get('number', -1), parserResult.get('offset', -1))