from rest_framework import serializers
from .models import UserNet


class GetUserNetSerializer(serializers.ModelSerializer):
    """ Вывод инфо о user
    """
    avatar = serializers.ImageField(read_only=True)

    class Meta:
        model = UserNet
        exclude = (
            "password",
            "last_login",
            "is_active",
            "is_staff",
            "is_superuser",
            "groups",
            "user_permissions"
        )


class GetUserNetPublicSerializer(serializers.ModelSerializer):
    """ Вывод публичной инфы о user
    """
    class Meta:
        model = UserNet
        exclude = (
            "email",
            "phone",
            "password",
            "last_login",
            "is_active",
            "is_staff",
            "is_superuser",
            "groups",
            "user_permissions"
        )


class UserByFollowerSerializer(serializers.ModelSerializer):
    """ Сериализация для подписчиков
    """
    avatar = serializers.ImageField(read_only=True)

    class Meta:
        model = UserNet
        fields = ('id', 'username', 'avatar')
