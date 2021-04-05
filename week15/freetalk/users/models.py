
# coding: utf-8

from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
import uuid


class ForumUserManager(BaseUserManager):

    def create_user(self, username, nickname, email, password):
        user = self.model(
            username=username,
            nickname=nickname,
            email=email,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user


class ForumUser(AbstractUser):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    nickname = models.CharField(verbose_name="昵称", max_length=128, unique=True)
    brief = models.TextField(verbose_name="简介", blank=True, default='')
    create_time = models.DateTimeField(auto_now_add=True)

    objects = ForumUserManager()

    class Meta:
        ordering = ['-create_time']

    def __str__(self):
        return f"<{self.username}:{self.nickname}>"
