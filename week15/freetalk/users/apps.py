
# coding: utf-8

from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    def ready(self):
        from .signals_handler import (
            on_article_created,
            on_comment_created,
        )
