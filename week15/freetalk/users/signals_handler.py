
# coding: utf-8

import logging
from django.dispatch import receiver
from django.db.models.signals import post_save
from article.models import Article
from comment.models import Comment
from .models import ForumUser
logger = logging.getLogger(__name__)


@receiver(post_save, sender=Article)
def on_article_created(sender, instance, created, **kwargs):
    if created is True:
        user = instance.user
        user.score += 1
        user.save()


@receiver(post_save, sender=Comment)
def on_comment_created(sender, instance, created, **kwargs):
    if created is True:
        user = instance.user
        user.score += 1
        user.save()
