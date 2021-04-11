from rest_framework import serializers
from .models import Article


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ("url", "id", "title", "body", "user", "view_count", "create_time", "update_time")
        read_only_fields = ["id", "user", "view_count", "create_time", "update_time"]
