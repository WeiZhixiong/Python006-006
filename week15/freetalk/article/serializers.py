from rest_framework import serializers
from .models import Article


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ("id", "title", "body", "author_id", "view_count", "create_time", "update_time")
        read_only_fields = ["id", "author_id", "view_count", "create_time", "update_time"]
