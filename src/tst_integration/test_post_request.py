import requests
from basic_integration_test import BasicIntegrationTest
from db_model import removeService

TEST_URL = '/instance/service'
VALID_NAME = 'test_servise_post'
EXIST_NAME = 'testservice'
DATA = {'name': VALID_NAME}
DATA2 = {'name': EXIST_NAME}
VALID_RESPONSE_TEXT = {}
EXIST_RESPONSE_TEXT = 'Service already exists'
VALID_RESPONSE_CODE = 200
NOT_VALID_RESPONSE_CODE = 400


class TestServiceListPostRequest(BasicIntegrationTest):

    def testServiceListPostRequest(self):
        response = requests.post(self.getUrl(TEST_URL), data=DATA)
        responseText = response.text
        responseCode = response.status_code
        self.assertEquals(2, responseText.find("$oid"))
        self.assertEquals(responseCode, VALID_RESPONSE_CODE)
        response = requests.post(self.getUrl(TEST_URL), data=DATA2)
        responseText = response.text
        responseCode = response.status_code
        self.assertEquals(responseText, EXIST_RESPONSE_TEXT)
        self.assertEquals(responseCode, NOT_VALID_RESPONSE_CODE)
        removeService(VALID_NAME)
