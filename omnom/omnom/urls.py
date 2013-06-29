from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
                       url(r'', include('social_auth.urls')),
                       url(r'', include('main.urls')),
)
