# coding: utf-8

from django.db import models
import uuid


class Comment(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    body = models.TextField(verbose_name="评论内容", max_length=256, blank=False)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    author_id = models.ForeignKey(
        'users.ForumUser',
        verbose_name="评论者id",
        related_name='comment_user',
        on_delete=models.CASCADE,
    )
    article_id = models.ForeignKey(
        "article.Article",
        verbose_name="文章id",
        related_name='article_comment',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.body
