import unittest
import sys
from test_tests_page import Test_tests_page
from test_PointListGet import TestPointListGet
# from test_GT_1703_GeocodingPluginReady import TestGeocodingPluginReady
from test_GT_1766_find_user_in_DB import TestGT1766FindUserInDB
from test_metadata_resource import TestMetadataResource
from basic_integration_test import BasicIntegrationTest
from test_user_list_resource import TestUserListResource
from test_plugin_list_resource import TestPluginListResource
from test_testplugin import TestTestPlugin
from test_status_request import TestStatusRequest
from test_delete_service_name import TestServiceDeleteRequest
from test_get_service_name import TestServiceGetRequest
from test_get_request import TestServiceListGetRequest
from test_put_service_name import TestServicePutRequest
from test_post_request import TestServiceListPostRequest
from test_service_name_get import TestServiceNameGetRequest
from test_get_channel_by_id import TestChannelGetRequest
from test_channel_service_get import TestChannelServiceGetRequest
from test_GT_1283_channels_service_post import TestChannelServicePostRequest
from test_channel_service_delete import ChannelResourceDelete
from test_channel_service_put import ChannelResourcePut
from test_instance_log import TestInstanceLogRequest
from test_point_resource_get import TestPointGetRequest
from test_debug_info_resource import TestDebugInfoResource
from test_logout_resource import TestLogoutResource
from test_GT_1320_point_resource_put import PointResourcePut
from test_delete_point_by_id import TestPointResourceDelete
from test_point_list_resource_post import TestPointListPostRequest
from test_GT_1386 import Test_GT_1386
from test_debug_login_resource import TestDebugLoginResource
from test_get_rout_map import TestRoutMap
from test_point_list_resource_get import TestPointListGet_ResponseText
from test_GT_1486_AfterRequesWriteInstanceLog import \
    TestAfterRequestWriteInstanceLog
from test_GT_1443_before_request import Test_GT_1443_Request
from test_GT_1442_manage_plugins import Test_GT_1442_managePlugins
from test_GT_1484_AfterRequestsStatusLogging import \
    TestAfterRequestStatusLogging
from test_internal_tests_page import Test_internal_tests_page
from test_ok_job_resource import Test_OKImportJob
from test_okimport_service_channel_not_exist import \
    Test_OKImportJob_not_exist
from test_GT_1511 import Test_GT_1511
from test_bc_parametr_point_list_post import TestBcParametrPointListPost
from test_GT_1590_extend_parse_parameters_for_point_list_resource\
    import TestExtendPointListParserWithFlagsBC
from test_GT_1697 import TestGT1697
# from test_GT_1732_GeocodingJobListResource import \
# TestGeocodingJobListResource
# from test_GT_1741_test_geocoder_import import TestGeocoderImport
from test_plugin_config_resource import TestPluginConfigResource
# from test_GT_1792_check_config_geocoder import \
#    TestPluginConfigGeocoder
from test_GT_1858_service_substr import TestServiceSearchBySubstr
from test_metadata_list_resource import TestMetadataListResource
from test_smartm3_plugin import TestSmartM3Plugin
from test_GT_2345_admin_log_resource import TestAdminLogResource


def main(host):
    suite = unittest.TestSuite()
    suite.addTest(
        BasicIntegrationTest.parametrize(
            TestMetadataResource, param=host))
    suite.addTest(
        BasicIntegrationTest.parametrize(
            TestUserListResource, param=host))
    suite.addTest(
        BasicIntegrationTest.parametrize(
            TestGT1766FindUserInDB,
            param=host))
    suite.addTest(
        BasicIntegrationTest.parametrize(
            TestGT1697,
            param=host))
    # suite.addTest(
    #    BasicIntegrationTest.parametrize(
    #        TestGeocodingPluginReady,
    #        param=host))
    # suite.addTest(
    #    BasicIntegrationTest.parametrize(
    #        TestGeocodingJobListResource,
    #        param=host))
    suite.addTest(
        BasicIntegrationTest.parametrize(
            TestPluginListResource,
            param=host))
    suite.addTest(
        BasicIntegrationTest.parametrize(
            TestTestPlugin,
            param=host))
    suite.addTest(
        BasicIntegrationTest.parametrize(
            TestPointListGet,
            param=host))
    suite.addTest(
        BasicIntegrationTest.parametrize(
            Test_tests_page,
            param=host))
    suite.addTest(
        BasicIntegrationTest.parametrize(
            TestChannelGetRequest,
            param=host))
    suite.addTest(
        BasicIntegrationTest.parametrize(
            TestStatusRequest,
            param=host))
    suite.addTest(
        BasicIntegrationTest.parametrize(
            TestServiceDeleteRequest,
            param=host))
    suite.addTest(
        BasicIntegrationTest.parametrize(
            TestServicePutRequest,
            param=host))
    suite.addTest(
        BasicIntegrationTest.parametrize(
            TestServiceListGetRequest,
            param=host))
    suite.addTest(
        BasicIntegrationTest.parametrize(
            TestServiceListPostRequest,
            param=host))
    suite.addTest(
        BasicIntegrationTest.parametrize(
            TestChannelServiceGetRequest,
            param=host))
    suite.addTest(
        BasicIntegrationTest.parametrize(
            TestServiceGetRequest,
            param=host))
    suite.addTest(
        BasicIntegrationTest.parametrize(
            TestServiceNameGetRequest,
            param=host))
    suite.addTest(
        BasicIntegrationTest.parametrize(
            TestChannelServicePostRequest,
            param=host))
    suite.addTest(
        BasicIntegrationTest.parametrize(
            ChannelResourceDelete,
            param=host))
    suite.addTest(
        BasicIntegrationTest.parametrize(
            ChannelResourcePut,
            param=host))
    suite.addTest(
        BasicIntegrationTest.parametrize(
            TestInstanceLogRequest,
            param=host))
    suite.addTest(
        BasicIntegrationTest.parametrize(
            TestPointGetRequest,
            param=host))
    suite.addTest(
        BasicIntegrationTest.parametrize(
            TestDebugInfoResource,
            param=host))
    suite.addTest(
        BasicIntegrationTest.parametrize(
            TestLogoutResource,
            param=host))
    suite.addTest(
        BasicIntegrationTest.parametrize(
            PointResourcePut,
            param=host))
    suite.addTest(
        BasicIntegrationTest.parametrize(
            TestPointResourceDelete,
            param=host))
    suite.addTest(
        BasicIntegrationTest.parametrize(
            TestPointListPostRequest,
            param=host))
    suite.addTest(
        BasicIntegrationTest.parametrize(
            TestAfterRequestWriteInstanceLog,
            param=host))
    suite.addTest(
        BasicIntegrationTest.parametrize(
            Test_GT_1386,
            param=host))
    suite.addTest(
        BasicIntegrationTest.parametrize(
            TestDebugLoginResource,
            param=host))
    suite.addTest(
        BasicIntegrationTest.parametrize(
            TestRoutMap,
            param=host))
    suite.addTest(
        BasicIntegrationTest.parametrize(
            TestAfterRequestStatusLogging,
            param=host))
    suite.addTest(
        BasicIntegrationTest.parametrize(
            TestPointListGet_ResponseText,
            param=host))
    suite.addTest(
        BasicIntegrationTest.parametrize(
            Test_GT_1443_Request,
            param=host))
    suite.addTest(
        BasicIntegrationTest.parametrize(
            Test_GT_1442_managePlugins,
            param=host))
    suite.addTest(
        BasicIntegrationTest.parametrize(
            Test_internal_tests_page,
            param=host))
    suite.addTest(
        BasicIntegrationTest.parametrize(
            Test_OKImportJob,
            param=host))
    suite.addTest(
        BasicIntegrationTest.parametrize(
            Test_OKImportJob_not_exist,
            param=host))
    suite.addTest(
        BasicIntegrationTest.parametrize(
            TestBcParametrPointListPost,
            param=host))
    suite.addTest(
        BasicIntegrationTest.parametrize(
            TestGT1697, param=host
        )
    )
    suite.addTest(
        BasicIntegrationTest.parametrize(
            TestPluginConfigResource, param=host
        )
    )
    suite.addTest(
        BasicIntegrationTest.parametrize(
            TestExtendPointListParserWithFlagsBC,
            param=host))
    suite.addTest(BasicIntegrationTest.parametrize(
        Test_GT_1511, param=host))
    # suite.addTest(BasicIntegrationTest.parametrize(
    #    TestPluginConfigGeocoder, param=host))
    # suite.addTest(
    #    BasicIntegrationTest.parametrize(
    #        TestGeocoderImport,
    #        param=host))
    suite.addTest(
        BasicIntegrationTest.parametrize(
            TestServiceSearchBySubstr,
            param=host))
    suite.addTest(
        BasicIntegrationTest.parametrize(
            TestMetadataListResource,
            param=host))
    suite.addTest(
        BasicIntegrationTest.parametrize(
            TestSmartM3Plugin,
            param=host))
    suite.addTest(
        BasicIntegrationTest.parametrize(
            TestAdminLogResource,
            param=host))
###################################################
# Place tests above this line ^^
###################################################
    returnCode = not unittest.TextTestRunner(
        verbosity=2).run(suite).wasSuccessful()

    sys.exit(returnCode)


if __name__ == '__main__':
    main(sys.argv[1])
