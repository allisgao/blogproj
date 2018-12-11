#! python3
# Author: George Gao, gaojz017@163.com

from ..models import Post, Category
from django import template
from django.db.models.aggregates import Count
from blog.models import Category

register = template.Library()


@register.simple_tag # 将函数 get_recent_posts 装饰为 register.simple_tag。这样就可以在模板中使用语法 {% get_recent_posts %} 调用这个函数了。
def get_recent_posts(num=5):
    """
    # 最新文档（最新5个）模板标签
    :param num:
    :return:
    """
    return Post.objects.all().order_by('created_time')[:num]

@register.simple_tag
def archives():
    """
    # 归档模板标签
    :return:
    """
    return Post.objects.dates('created_time', 'month', order='DESC')

@register.simple_tag
def get_categories():
    """
    # 分类模板标签
    :return:
    """
    return Category.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)

