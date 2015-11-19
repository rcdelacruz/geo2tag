QUnit.test('date_search macros test', function( assert ) {
    var done = assert.async(); 
    var date_search_id = 'date_search', value = '1.01.1990', changeValue = '1.01.1991';
    var date_search = new dateSearch('date_search');

    assert.equal(date_search_id, date_search.macroId);

    date_search.setValueDateBegin(value);
    assert.equal(date_search.getValueDateBegin(), value);
    date_search.setValueDateEnd(value);
    assert.equal(date_search.getValueDateEnd(), value);
    
    date_search.clearDateBegin()
    date_search.clearDateEnd()
    assert.equal(date_search.getValueDateBegin(), '');
    assert.equal(date_search.getValueDateEnd(), '');

    function myChangeDateBegin() {
        assert.equal(true, true);
        done();
    }
    function myChangeDateEnd() {
        assert.equal(true, true);
        done();
    }
    date_search.changeDateBegin(myChangeDateBegin);
    date_search.jqueryObjectDateBegin.val('value').trigger('change');
    date_search.changeDateEnd(myChangeDateEnd);
    date_search.jqueryObjectDateEnd.val('value').trigger('change');
});
