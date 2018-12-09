#! python3
# Author: George Gao, gaojz017@163.com

from django.conf.urls import url
from . import views

app_name = 'blog'   # 通过 app_name='blog' 告诉 Django 这个 urls.py 模块是属于 blog 应用的，这种技术叫做视图函数命名空间。
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),  # 首页
    url(r'^post/(?P<pk>[0-9]+)/$', views.PostDetailView.as_view(), name='detail'),    # 详情页
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', \
        views.ArchivesView.as_view(), name='archives'),   # 归档
    url(r'category/(?P<pk>[0-9]+)/$', views.CategoryView.as_view(), name='category'), # 分类
]
