# coding: utf-8

from django.db import models
import uuid


class Article(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    title = models.CharField(verbose_name="文章标题", max_length=128)
    body = models.TextField(verbose_name="文章内容", blank=True, default='')
    view_count = models.BigIntegerField(verbose_name="阅读数", default=0)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(
        'users.ForumUser',
        verbose_name="作者",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"<{self.title}>"
