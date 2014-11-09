from django.conf.urls import patterns, include, url
from django.contrib import admin
from ashrams.views import sample_html

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^home/', sample_html),
    # url(r'^reports/', include('Outbreak.weburls')),
    url(r'^reports/', include('myuser.weburls')),
    # url(r'^reports/', include('SecretKey.urls')),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
    url(r'^api-token-auth/', 'rest_framework.authtoken.views.obtain_auth_token'),
    # url(r'^admin/Outbreak/', include('Outbreak.urls')),
    # url(r'^admin/Rehydration/', include('Rehydration.urls')),
    url(r'^admin/', include(admin.site.urls)),

)