from rest_framework import generics, viewsets
from .serializers import ForumUserSerializer
from .models import ForumUser
from .permissions import IsOwner
from rest_framework.views import APIView


class RegisterForumUser(generics.CreateAPIView):
    queryset = ForumUser.objects.all()
    serializer_class = ForumUserSerializer


class ForumUserViewSet(viewsets.ModelViewSet):
    queryset = ForumUser.objects.all()
    serializer_class = ForumUserSerializer
    permission_classes = [IsOwner]
