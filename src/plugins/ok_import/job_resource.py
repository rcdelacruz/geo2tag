from possible_exception import possibleException
from flask_restful import reqparse
from flask.ext.restful import Resource
from job_manager import JobManager
from ok_import_resource_parser import OKImportParser
from thread_job import ThreadJob
from open_karelia_import import openKareliaImport
import sys
sys.path.append('../')
from db_model import getChannelByName,getServiceIdByName


class JobResource(Resource):

    @possibleException
    def get(self, serviceName):
        getServiceIdByName(serviceName)
        return JobManager.getJobs()

    @possibleException
    def post(self, serviceName):
        job = OKImportParser.parsePostParameters()
        chlName = job.get('channelName') 
        getServiceIdByName(serviceName)
        getChannelByName(serviceName,chlName)
        job = ThreadJob(openKareliaImport, channelName, openDataUrl, showObjectUrl, showImageUrl, serviceName)
        JobManager.createJob(job)
        thread = ThreadJob(openKareliaImport, job.get('channelName'), \
                           job.get('openDataUrl'), \
                           job.get('showObjectUrl'), \
                           job.get('showImageUrl'), \
                           serviceName)

        return JobManager.startJob(thread)
