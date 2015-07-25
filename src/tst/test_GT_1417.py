import unittest
import sys
import os
from flask import Flask
from flask.ext.restful import Api
sys.path.append('../')
from main import initApp
from plugins import getPluginList
class TestGt1417(unittest.TestCase):
    def testGt1417(self):
        app = Flask(__name__)
        api = Api(app)
        os.chdir('..')
        initApp(api)
        os.chdir('../..')
        resources = api.endpoints
        print resources, '0000000000000000000000'
        self.assertTrue('resource_gt_1416' in resources)
        self.assertTrue('resource_gt_1417' in resources)
        os.chdir('tst')
