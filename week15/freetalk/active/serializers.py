from rest_framework import serializers
from .models import Active


class ActiveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Active
        fields = "__all__"
