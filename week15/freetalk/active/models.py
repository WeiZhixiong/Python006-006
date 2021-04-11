# coding: utf-8

from django.db import models


class Active(models.Model):
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="发布时间")
    user = models.ForeignKey(
        'users.ForumUser',
        verbose_name="用户",
        on_delete=models.CASCADE,
        null=True
    )
    article = models.ForeignKey(
        "article.Article",
        verbose_name="文章",
        on_delete=models.CASCADE,
        null=True
    )
    comment = models.ForeignKey(
        'comment.Comment',
        verbose_name="评论",
        on_delete=models.CASCADE,
        null=True
    )

    def __str__(self):
        return f"<user: {self.user}; article:{self.article}; comment:{self.comment}>"
