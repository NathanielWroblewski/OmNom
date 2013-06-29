from django.conf.urls import patterns, include, url

urlpatterns = patterns('main.views',
                       url(r'^test-page/$','test_page',name="test_page"),
                       url(r'^actions/fulfill-request/(?P<request_id>[^/]+)/$', 'actions_fulfill_request',name="actions_fulfill_request"),
                       url(r'^actions/confirm-request/(?P<request_id>[^/]+)/$', 'actions_confirm_request',name="actions_confirm_request"),
                       url(r'^actions/pickup-request/(?P<request_id>[^/]+)/$', 'actions_pickup_request',name="actions_pickup_request"),
                       url(r'^home/$', 'home',name="home"),
                       url(r'^messenger/donation_map$', 'donation_map',name="donation_map"),
)
