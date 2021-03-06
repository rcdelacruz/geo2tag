from possible_exception import possibleException
from flask_restful import Resource
from flask import render_template
from flask import make_response
from db_model import getNotEmptyChannelIds
from map_resource_parser import MapParser


CHANNEL_IDS = 'channel_ids'


class MapResource(Resource):

    @possibleException
    def get(self, serviceName=None):
        args = MapParser.parseGetParameters()
        result = {CHANNEL_IDS: []}
        if args[CHANNEL_IDS] is None:
            result.update(getDefaultChannelIds(serviceName))
        return make_response(
            render_template(
                'map.html',
                params=result))


def getDefaultChannelIds(serviceName):
    result = {}
    all_channel_ids = getNotEmptyChannelIds(serviceName)
    result[CHANNEL_IDS] = all_channel_ids
    return result
