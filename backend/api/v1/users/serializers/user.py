from rest_framework import serializers

from api.v1.users.constants import (
    USER_PASSWORD_MAX_LENGTH,
    USER_PASSWORD_MIN_LENGTH,
)
from applications.users.models import User

__all__ = ["UserSerializer", "UserShortInfoSerializer"]


class UserShortInfoSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(
        source="public_id",
        read_only=True,
        format="hex",
    )

    class Meta:
        model = User
        fields = (
            "id",
            "first_name",
            "last_name",
            "username",
            "status",
            "bio",
            "photo",
        )


class UserSerializer(UserShortInfoSerializer):
    data_joined = serializers.DateTimeField(read_only=True)
    last_updated = serializers.DateTimeField(read_only=True)
    password = serializers.CharField(
        min_length=USER_PASSWORD_MIN_LENGTH,
        max_length=USER_PASSWORD_MAX_LENGTH,
        write_only=True,
        required=True,
    )

    class Meta(UserShortInfoSerializer.Meta):
        model = User
        fields = UserShortInfoSerializer.Meta.fields + (
            "email",
            "password",
            "data_joined",
            "last_updated",
            "is_active",
            "is_vip",
            "is_blocked",
            "is_admin",
            "is_moder",
        )
        read_only_fields = (
            "is_active",
            "is_vip",
            "is_blocked",
            "is_admin",
            "is_moder",
        )
