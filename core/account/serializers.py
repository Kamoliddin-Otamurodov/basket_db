from rest_framework import serializers
from .models import UserData


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserData
        fields = ["id", "username", "first_name", "password"]

    def create(self, validated_data: dict) -> UserData:
        user = UserData.objects.create(
            username=validated_data['username']
        )
        user.first_name = validated_data.get('first_name', user.first_name)
        user.set_password(validated_data['password'])
        user.save()
        return user