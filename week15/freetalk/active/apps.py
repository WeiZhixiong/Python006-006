from django.apps import AppConfig


class ActiveConfig(AppConfig):
    name = 'active'

    def ready(self):
        from .signals_handler import (
            on_article_created,
            on_comment_created,
        )
