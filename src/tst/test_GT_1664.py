from unittest import TestCase
from ok_import_resource_parser import OKImportParser
from thread_job import ThreadJob
from open_karelia_import import openKareliaImport
from job_list_resource_factory import JobListResourceFactory


class TestJobListResourceFactory(TestCase):

    def testobListResourceFactory(self):
        self.assertEquals(
            "<class 'job_list_resource_factory.JobListResource'>",
            unicode(
                JobListResourceFactory(
                    OKImportParser,
                    ThreadJob,
                    openKareliaImport
                )
            )
        )
