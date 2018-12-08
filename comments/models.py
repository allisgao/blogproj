from django.db import models


class Comment(models.Model):
    """
    # 评论是关联到某篇文章（Post）的，由于一个评论只能属于一篇文章，一篇文章可以有多个评论，是一对多的关系，因此这里我们使用了 ForeignKey。
    """
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    url = models.URLField(blank=True)
    text = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    post = models.ForeignKey('blog.Post')

    def __str__(self):
        return self.text[:20]