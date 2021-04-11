from django.urls import path
from .views import RegisterForumUser, ForumUserViewSet

user_detail = ForumUserViewSet.as_view({
    'get': 'retrieve',
    'patch': 'partial_update'
})


urlpatterns = [
    path('register', RegisterForumUser.as_view(), name='user-register'),
    path('<uuid:pk>', user_detail, name='user_detail'),
]
