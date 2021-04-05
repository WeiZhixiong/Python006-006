from django.urls import path
from .views import RegisterForumUser

user_register = RegisterForumUser.as_view()


urlpatterns = [
    path('register', RegisterForumUser.as_view(), name='user-register')
]
