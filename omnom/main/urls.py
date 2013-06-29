from django.conf.urls import patterns, include, url

urlpatterns = patterns('main.views',
                       url(r'^test-page/$','test_page',name="test_page"),
                       url(r'^actions/fulfill-request/(?P<request_id>[^/]+)/$', 'actions_fulfill_request',name="actions_fulfill_request"),
                       url(r'^actions/confirm-request/(?P<request_id>[^/]+)/$', 'actions_confirm_request',name="actions_confirm_request"),
                       url(r'^actions/twilio_callback/', 'twilio_callback',name="twilio_callback"),
                       url(r'^actions/pickup-request/(?P<request_id>[^/]+)/$', 'actions_pickup_request',name="actions_pickup_request"),
                       url(r'^$', 'home',name="home"),
                       url(r'^create_profile/$', 'create_profile',name="create_profile"),
                       url(r'^messenger/donation_map$', 'donation_map',name="donation_map"),
                       url(r'^requests/$', 'requests',name="requests"),
                       url(r'^person/$', 'get_pic_url',name="get_pic_url"),
                       url(r'^messenger/direction_map$', 'direction_map',name="direction_map"),
                       url(r'^messenger/confirmation$', 'msg_confirmation',name="msg_confirmation"),
                       url(r'^create_pickup_request/$', 'create_pickup_request',name="create_pickup_request"),
                       url(r'^messenger/feedback$', 'feedback',name="feedback"),
                       url(r'^messenger/picked_up$', 'picked_up',name="picked_up"),
)
