# coding: utf-8

from django.db import models
import uuid


class Comment(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    body = models.TextField(verbose_name="评论内容", max_length=256, blank=False)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(
        'users.ForumUser',
        verbose_name="评论者",
        on_delete=models.CASCADE,
    )
    article = models.ForeignKey(
        "article.Article",
        verbose_name="文章",
        on_delete=models.CASCADE,
    )
    relay_comment = models.ForeignKey(
        'self',
        verbose_name="回复对象",
        on_delete=models.CASCADE,
        null=True
    )

    def __str__(self):
        return self.body
