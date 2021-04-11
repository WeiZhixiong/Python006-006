from rest_framework import viewsets
from .models import Article
from .serializers import ArticleSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from common.permissions import IsOwnerOrReadOnly


class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['title', 'body']
    search_fields = filterset_fields

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def retrieve(self, request, *args, **kwargs):
        article = self.get_object()
        serializer = self.get_serializer(article)
        resp_data = serializer.data
        # ¸üÐÂÔÄ¶ÁÊý
        article.view_count += 1
        article.save()
        return Response(resp_data)
