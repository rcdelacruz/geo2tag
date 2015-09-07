from unittest import TestCase
import sys
sys.path.append('../../scripts/performance/od_performance')
from test_performance import main

CREATE_JOB_LINK = 'http://geomongo/instance/plugin/ok_import/service/testservice/job'
JOB_DATA = '{"channelName":"testchannel","openDataUrl":"http://mobile.openkarelia.org//get_nearest_objects?latitude=61.787458487564&longitude=34.362810647964", "showObjectUrl":"", "showImageUrl":""} '
VIEW_JOB_LINK = 'http://geomongo/instance/plugin/ok_import/service/testservice/job'
JOB_COUNT = 1
TIMEOUT = 5

class test_GT_1578testPerfomance(TestCase):

    def test_GT_1578testPerfomance(self):
        ans = main(CREATE_JOB_LINK, JOB_DATA, VIEW_JOB_LINK, JOB_COUNT, TIMEOUT)
        self.assertEquals(1, ans)

