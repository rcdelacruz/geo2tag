from pymongo import MongoClient
from config_reader import getHost, getPort, getDbName
import pymongo
from datetime import datetime
from  service_not_found_exception import ServiceNotFoundException
from service_already_exists_exception import ServiceAlreadyExistsException
from pymongo import Connection
from bson.objectid import ObjectId
from bson.errors import InvalidId
from channel_does_not_exist import ChannelDoesNotExist
from point_does_not_exist import PointDoesNotExist

# getLog constants
COLLECTION_LOG_NAME = "log"
FIND_AND_SORT_KEY = "date"

# getPointById constants
COLLECTION_POINTS_NAME = "points"
POINTS_FIND_AND_KEY = "_id"

#updateService constants
COLLECTION_SERVICES_NAME = "services"
COLLECTION_SERVICES_EL_CONFIG_NAME = "config"


# Collections
TAGS = 'tags'
COLLECTION = 'services'
NAME = 'name'
CONFIG = 'config'
LOG_SIZE = 'log_size'
OWNERID = 'owner_id'
ID = '_id'
LOG = 'log'
#db initialisation
MONGO_CLIENT = None#MongoClient(getHost(), getPort())

db = MongoClient(getHost(), getPort())[getDbName()]
#keys
USER_ID = 'user_id'
DATE = 'date'
MESSAGE = 'message'
SERVICE = 'service'
COLLECTION = 'services'
CHANNELS_COLLECTION = 'channels'
POINTS_COLLECTION = 'points'
JSON = 'json'
ACL = 'acl'
OWNER_GROUP = 'owner_group'
POINTS_COLLECTION = 'points'
LOCATION = 'location'
TYPE = 'type'
POINT = 'Point'
COORDINATES = 'coordinates'
LON = 'lon'
LAT = 'lat'
ALT = 'alt'
CHANNEL_ID = 'channel_id'

def addLogEntry(dbName, userId, message, service='instance'):
    currentDate = datetime.now().isoformat()
    collection = getDbObject(dbName) [LOG]
    if dbName == getDbName():
        collection.save({USER_ID : userId, DATE : currentDate, MESSAGE : message, SERVICE : service})
    else:
        collection.save({USER_ID : userId, DATE : currentDate, MESSAGE : message})

def possibleException(func):
    def funcPossibleException(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except BaseException as e:
            if hasattr(e, 'getReturnObject'):
                return e.getReturnObject()
            else:
                raise
    return funcPossibleException

def addTag(tag):
    getDbObject()[TAGS].insert(tag)

def addService(name, logSize, ownerld):
    db = getDbObject()
    try:
        obj = getServiceIdByName(name)
        raise ServiceAlreadyExistsException()
    except ServiceNotFoundException as e:
        obj_id = db[COLLECTION].save({NAME : name, CONFIG : {LOG_SIZE : logSize}, OWNERID : ownerld})
        if obj_id == None:
            return None
        else:
            return obj_id


def getLog(dbName, number, offset, dateFrom, dateTo) :
    db = getDbObject(dbName)
    collection = db[COLLECTION_LOG_NAME]
    if collection.count() == 0 :
        return []
    number = 0 if (number == None or number < 0) else number
    offset = 0 if (offset == None or offset < 0) else offset
    if (dateFrom == None and dateTo == None) :
        return []
    elif dateFrom == None :
        return collection.find({FIND_AND_SORT_KEY : {"$lte" : dateTo}}, None, offset, number).sort(FIND_AND_SORT_KEY, pymongo.ASCENDING)    
    elif dateTo == None :
        return collection.find({FIND_AND_SORT_KEY : {"$gte" : dateFrom}}, None, offset, number).sort(FIND_AND_SORT_KEY, pymongo.ASCENDING)
    else :
        if dateFrom > dateTo :
            return []
        return collection.find({FIND_AND_SORT_KEY : { "$gte" : dateFrom , "$lte" : dateTo}}, None, offset, number).sort(FIND_AND_SORT_KEY, pymongo.ASCENDING)

def updateService(name, config) :
    services_collection = db[COLLECTION_SERVICES_NAME]
    for el in config :
        tmp_el_to_set = COLLECTION_SERVICES_EL_CONFIG_NAME + '.' + str(el)
        services_collection.update(
            {"name" : name},
            #changes will affect on service's sub-document called 'config'
            #if there is no such sub-document called 'config', it will be created
            {"$set" : {tmp_el_to_set : config[el]}},
            #changes will affect on all services with name mentioned above
            multi = True
        )
    #changed service(s) cursor in return
    return services_collection.find({"name" : name})

def getServiceIdByName(name):
    obj = getDbObject()[COLLECTION].find_one({NAME : name})
    print obj
    if obj != None:
        return obj
    raise ServiceNotFoundException()

def removeService(name):
    try:
        obj = getServiceIdByName(name)
        db[COLLECTION].remove({ID : obj['_id']})
        connection = Connection()
        connection.drop_database(name)
    except ServiceNotFoundException as e:
        raise

def getServiceById(id):
    obj = getDbObject()[COLLECTION].find_one({ID : id})
    if obj != None:
        return obj
    raise ServiceNotFoundException()

def getServiceList(number, offset):
    db = getDbObject()
    if number is None:
        number = db[COLLECTION].count()
    if offset is None:
        offset = 0
    result = list(db[COLLECTION].find().sort(NAME, 1).skip(offset).limit(number))
    return result

def getChannelsList(serviceName, substring, number, offset):
    db = getDbObject(serviceName)
    if substring != None and number is not None and offset is not None:
       return db[CHANNELS_COLLECTION].find({'name':{'$regex':substring}}).skip(offset).limit(number)
    elif substring != None and offset != None:
        return db[CHANNELS_COLLECTION].find({'name':{'$regex': substring}}).skip(offset)
    elif substring != None and number != None:
        return db[CHANNELS_COLLECTION].find({'name':{'$regex': substring}}).limit(number)
    elif offset is not None and number != None:
        return db[CHANNELS_COLLECTION].find().skip(offset).limit(number)
    elif substring != None:
        return db[CHANNELS_COLLECTION].find({'name':{'$regex': substring}})
    elif number is not None:
        return db[CHANNELS_COLLECTION].find().limit(number)
    elif offset is not None:
        return db[CHANNELS_COLLECTION].find().skip(offset)

def getChannelById(serviceName, channelId):
    db = getDbObject(serviceName)
    if isinstance(channelId, str) or isinstance(channelId, unicode):
        obj = db[CHANNELS_COLLECTION].find_one({'_id': ObjectId(channelId)})
    else:
        obj = db[CHANNELS_COLLECTION].find_one({'_id': channelId})
    if obj != None:
        return obj
    raise ChannelDoesNotExist()

def getDbObject(dbName = getDbName()):
    return getClientObject()[dbName]

def getClientObject():
    global MONGO_CLIENT
    if MONGO_CLIENT == None:
        MONGO_CLIENT = MongoClient(getHost(), getPort())
#    print "getClientObject: {0}".format(hex(id(MONGO_CLIENT)))
    return MONGO_CLIENT

def deleteChannelById(serviceName, channelId):
    db = getDbObject(serviceName)
    if isinstance(channelId, str) or isinstance(channelId, unicode):
        result = list(db[CHANNELS_COLLECTION].find({'_id': ObjectId(channelId)}))
    else:
        result = list(db[CHANNELS_COLLECTION].find({'_id': channelId}))
    if len(result) > 0:
        db[CHANNELS_COLLECTION].remove({'_id': channelId})
    else:
        raise ChannelDoesNotExist()

def addChannel(name, json, owner_id, serviceName):
    db = getDbObject(serviceName)
    return db[CHANNELS_COLLECTION].insert({NAME: name, JSON: json, OWNERID: owner_id, OWNER_GROUP: 'STUB', ACL: 777})

def updateChannel(serviceName, channelId, name, json, acl):
    db = getDbObject(serviceName)
    try:
        obj = db[CHANNELS_COLLECTION].find_one({ID: ObjectId(channelId)})
    except:
        raise ChannelDoesNotExist()
    if obj == None:
        raise ChannelDoesNotExist()
    else:
        obj['name'] = name
        if json != None:
            obj['json'] = json
        if acl != None:
            obj['acl'] = acl
        db[CHANNELS_COLLECTION].save(obj)

def getChannelByName(serviceName, channelName):
    db = getDbObject(serviceName)
    obj = db[CHANNELS_COLLECTION].find_one({NAME: channelName})
    if obj != None:
        return obj
    raise ChannelDoesNotExist()

def deletePointById(serviceName, pointId):
    db = getDbObject(serviceName)
    obj = db[POINTS_COLLECTION].find_one({ID: ObjectId(pointId)})
    if obj != None:
        db[POINTS_COLLECTION].remove({ID: ObjectId(pointId)})
    else:
        raise PointDoesNotExist()

def getPointById(serviceName, pointId) :
    pointsCollection = getDbObject(serviceName)[COLLECTION_POINTS_NAME]
    point = pointsCollection.find_one({POINTS_FIND_AND_KEY : ObjectId(str(pointId))})
    if point != None :
        return point
    raise PointDoesNotExist()

def addPoints(serviceName, pointsArray):
    db = getDbObject(serviceName)[COLLECTION_POINTS_NAME]
    for point in pointsArray:
        obj = {}
        obj[JSON] = point[JSON]
        obj[LOCATION] = {TYPE: POINT, COORDINATES: [point[LON], point[LAT]]}
        obj[ALT] = point[ALT]
        obj[CHANNEL_ID] = point[CHANNEL_ID]
        obj[DATE] = datetime.now()
        db.save(obj)

def updatePoint(serviceName, pointId, changes):
    db = getDbObject(serviceName)
    try:
        obj = db[POINTS_COLLECTION].find_one({ID: ObjectId(pointId)})
    except:
        raise PointDoesNotExist()
    if obj == None:
        raise PointDoesNotExist()
    else:
        for key in changes.keys():
            if key in obj.keys():
                obj[key] = changes[key]
        db[POINTS_COLLECTION].save(obj)
    print obj

def addServiceDb(dbName):
    db = getDbObject(dbName)
    pymongo.GEOSPHERE = '2dsphere'
    pymongo.DESCENDING = -1
    db[COLLECTION_POINTS_NAME].ensure_index([("location", pymongo.GEOSPHERE)])
    db[COLLECTION_POINTS_NAME].create_index([("date", pymongo.DESCENDING)])

def findPoints(serviceName, channel_ids, number, geometry=None, altitude_from=None, altitude_to=None, substring=None, date_from=None, date_to=None, offset=None, radius=1000):
    db = getDbObject(serviceName)
    points = []
    for channel_id in channel_ids:
        obj = db[POINTS_COLLECTION].find_one({CHANNEL_ID: channel_id, ALT: {'$lte': altitude_from}, ALT: {'$lte': altitude_to}})
        if obj != None:
            points.append(obj)
    return points