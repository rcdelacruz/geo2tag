from flask_restful import request
from json import loads

JSON = 'JSON'

class PluginConfigResourceParser():

    @staticmethod
    def parsePostParameters():
        args = loads(request.get_data())
        return args
