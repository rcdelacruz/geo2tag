from flask_restful import Resource
from flask import render_template
from possible_exception import possibleException
from icon_resource_parser import IconResourceParser, CHANNEL_ID
import hashlib


class IconResource(Resource):

    @possibleException
    def get(self):
        args = IconResourceParser.parseGetParameters()
        color = getColorsFromChannelId(args[CHANNEL_ID])
        return render_template("icon.svg", color = color)


def getColorsFromChannelId(channel_id):
    hdigest = hashlib.md5(channel_id).hexdigest()
    colors = hdigest[:6]
    return colors
