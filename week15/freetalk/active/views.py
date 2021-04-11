from rest_framework import generics
from .models import Active
from .serializers import ActiveSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class ActiveList(generics.ListAPIView):
    serializer_class = ActiveSerializer
    queryset = Active.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['user']
    search_fields = filterset_fields
