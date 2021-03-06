from flask_restful import reqparse


GET_ARGS_NUMBER = 'number'
GET_ARGS_OFFSET = 'offset'
GET_ARGS_LOGIN = 'login'


class Userlistresourceparser():

    @staticmethod
    def parseGetParameters():
        parser = reqparse.RequestParser()
        parser.add_argument(GET_ARGS_NUMBER, type=int, default=None)
        parser.add_argument(GET_ARGS_OFFSET, type=int, default=None)
        parser.add_argument(GET_ARGS_LOGIN, type=str, default=None)
        args = parser.parse_args()
        return args
