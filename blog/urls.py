#! python3
# Author: George Gao, gaojz017@163.com

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),

]
