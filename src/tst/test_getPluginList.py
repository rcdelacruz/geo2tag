import unittest
import sys
import os
sys.path.append('../')
from plugin_routines import getPluginList


class TestGetPluginList(unittest.TestCase):
    def testGetPluginList(self):
        print 'Before testGetPluginList {0}'.format(os.getcwd())
        os.chdir('../')
        pluginsList = getPluginList()
        print pluginsList
        root, dirs, files = os.walk('plugins').next()
        os.chdir('tst/')
        self.assertEquals(dirs, pluginsList)
