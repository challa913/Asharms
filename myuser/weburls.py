from myuser.views import CreateMyUserView, MyUserDetailView

__author__ = 'challa'

from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = []

urlpatterns += format_suffix_patterns(
    patterns('myuser.views',
        url(r'^myuser/$', CreateMyUserView.as_view(),name='user-signup'),
        url(r'^myuser/(?P<pk>[-._a-zA-Z0-9]+)/$', MyUserDetailView.as_view(), name='user-detail')
    )
)