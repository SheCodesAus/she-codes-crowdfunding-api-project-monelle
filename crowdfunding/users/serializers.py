from rest_framework import serializers
from .models import CustomUser


class CustomUserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    username = serializers.CharField(max_length=200)
    email = serializers.CharField(max_length=200)
    about = serializers.CharField(max_length=500)
    profile_pic = serializers.URLField()


    def create(self, validated_data):
        return CustomUser.objects.create(**validated_data)