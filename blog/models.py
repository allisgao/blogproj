from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
import markdown
from django.utils.html import strip_tags
from django.utils import timezone

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
    tags = models.ManyToManyField(Tag)
    # 作者。
    author = models.ForeignKey(User)
    # page view文章页面浏览次数
    p_views = models.PositiveIntegerField(default=0)

    def __str__(self):
        if len(self.title) > 25:
            return self.title[:25] + "..."
        else:
            return self.title

    def get_absolute_url(self):
        # 自定义 get_absolute_url 方法
        # 记得从 django.urls 中导入 reverse 函数
        return reverse('blog:detail', kwargs={'pk': self.pk})
    def increase_views(self):
        self.p_views += 1
        self.save(update_fields=['p_views'])

    def save(self, *args, **kwargs):
        """
        # 自动保存摘要
        :param args:
        :param kwargs:
        :return:
        """
        if not self.excerpt:
            md = markdown.Markdown(extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
            ])
            # 先将 Markdown 文本渲染成 HTML 文本
            # strip_tags 去掉 HTML 文本的全部 HTML 标签
            # 从文本摘取前 54 个字符赋给 excerpt
            excerpt0 = strip_tags(md.convert(self.body))
            self.excerpt = excerpt0[:100] + '...' if len(excerpt0)> 100 else excerpt0
            # self.excerpt = strip_tags(md.convert(self.body))[:54]
            # 调用父类的 save 方法将数据保存到数据库中
            super(Post, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-created_time', 'title']