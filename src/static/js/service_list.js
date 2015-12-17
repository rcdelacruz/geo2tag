var Service = Backbone.Model.extend({});

var service = new Service({
    title: "Service"
});

var ServiceList = Backbone.Collection.extend({
    model: Service,
    url: function(){
        var number = 5;
        return '/instance/service?number=' + number;
    }
});

var ServiceView = Backbone.View.extend({
    tagName: "div",
    id: "container_service_list",
    render: function(json) {
        $('#' + this.id).append(get_service_display(json));
        return this;
    }
});

service_view = new ServiceView({'model' : service});

var ServicePageModel = Backbone.Model.extend({
    initialize: function() {
        this.services = new ServiceList();       
    }
});

service_list_page = new ServicePageModel;

var ServicePageView = Backbone.View.extend({
    initialize: function() {
        this_ = this;
        this.model.fetch({
            success: function(){
                this_.render();
            }
        });
    },
    render: function() {
        for(var i = 0; i < this.model.length; i++)
            service_view.render(this.model.at(i).attributes);
    }
});

var service_page = new ServicePageView({model: service_list_page.services});

function get_service_display(json){
    var service_name = json.name;
    var service_id = json._id.$oid;
    var service_link = getUrlWithPrefix('/admin/service/');
    var result = '<div class="row" id="' + service_id + '"><div class="col-xs-8"><h3><a href = ' + service_link + service_id + '>' + service_name + '</a></h3></div>';
    result += '<div class="col-xs-4"><button type="button" class="btn btn-primary btn-lg" service_id="' + service_id + '">DELETE</button></div></div>';
    return result;
}

urlBuilder = new UrlBuilder('/instance/service?',  {'number':10, 'offset':0});
urlBuilder.setParameterOnChangeListener('offset', pagination.setOnChangeListener, pagination.getPageNumber);


urlBuilder.onChange(function(){
    service_list_page.url = this.getUrl();
    service_list_page.refresh(); //?
});
