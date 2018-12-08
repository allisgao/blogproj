#! python3
# Author: George Gao, gaojz017@163.com

from django.conf.urls import url
from . import views

app_name = 'comments'
urlpatterns = [
    url(r'comments/post/(?P<post_pk>[0-9]+)/$', views.post_comment, name='post_comment'),
]