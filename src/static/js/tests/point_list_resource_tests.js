var point_list_resource_tests = {
    'GET':{
        data:{'number':100,'channel_ids':'556721a52a2e7febd2744202','channel_ids':'556721a52a2e7febd2744201','altitude_from':1.1,'date_from' : '2015-09-10T23:32:17.000000','date_to' : '2015-09-11T23:32:17.000000','bc_from':'true','bc_to':'true'},
        url : '/' + getInstancePrefix() + '/service/testservice/point'
    },
    'POST':{
        data:{'lat':1.1, 'lon':1.1,  'alt':1.1,  'json':{'a':'b'}, 'channel_id':'556721a52a2e7febd2744202'},
        url : '/' + getInstancePrefix() + '/service/testservice/point'
    }
};

QUnit.test( 'GET ' + point_list_resource_tests.GET.url + JSON.stringify(point_list_resource_tests.GET.data), function( assert ) {
    var done = assert.async(); 
    var getCallbackFail = function() {
        assert.ok(false, 'GET failed' );
        done();
    };
    var getCallbackSuccess = function() {
        assert.ok(true, 'GET success' );
        done();
    };
    $.get(point_list_resource_tests.GET.url, point_list_resource_tests.GET.data )
        .fail(getCallbackFail).done(getCallbackSuccess);
 
});

QUnit.test( 'POST ' + point_list_resource_tests.POST.url + JSON.stringify(point_list_resource_tests.POST.data), function( assert ) {
    var done = assert.async(); 
    var postCallbackFail = function() {
        assert.ok(false, 'POST failed' );
        done();
    };
    var postCallbackSuccess = function() {
        assert.ok(true, 'POST success' );
        done();
    };
    $.post(point_list_resource_tests.POST.url,JSON.stringify([point_list_resource_tests.POST.data]))
    .done(postCallbackSuccess) 
    .fail(postCallbackFail);
});
