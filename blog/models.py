from django.db import models
from django.contrib.auth.models import User

"""
Category: 分类
Tag： 标签
Post： 文章
"""

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Post(models.Model):
    # 标题
    title = models.CharField(max_length=100)
    # 正文
    body = models.TextField()
    # 时间，创建时间和修改时间
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    # 文章摘要
    excerpt = models.CharField(max_length=200, blank=True)
    # 分类和标签。这里，规定一篇文章只能有一个分类，但可以有多个标签。
    ## 分类。一篇文章只有一个分类，一个分类下可以有多篇文章
    category = models.ForeignKey(Category)
    ## 标签。一篇文章可以有多个分类，一个分类下也可以有多篇文章
    tags = models.ManyToManyField(Tag, blank=True)
    # 作者。
    author = models.ForeignKey(User)

    def __str__(self):
        return self.title
