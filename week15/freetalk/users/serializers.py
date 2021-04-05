from rest_framework import serializers
from .models import ForumUser


class ForumUserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = ForumUser
        fields = ('id', 'username', 'nickname', 'password', 'brief')
        read_only_fields = ['id', 'create_time']
        extra_kwargs = {
            'password': {'write_only': True, 'required': True},
        }

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = ForumUser(**validated_data)
        user.set_password(password)
        user.save()
        return user
