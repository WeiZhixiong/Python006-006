from rest_framework import generics
from .serializers import ForumUserSerializer
from .models import ForumUser


class RegisterForumUser(generics.CreateAPIView):
    queryset = ForumUser.objects.all()
    serializer_class = ForumUserSerializer
