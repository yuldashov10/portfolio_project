from typing import Any

USER_SERIALIZER: str = "api.v1.users.serializers.UserSerializer"

IS_USER_OWNER_OR_ADMIN_SERIALIZER: str = (
    "api.v1.users.permissions.IsOwnerOrAdmin"
)

DJOSER: dict[str, Any] = {
    "LOGIN_FIELD": "username",
    "HIDE_USERS": False,
    "USER_CREATE_PASSWORD_RETYPE": True,
    "ACTIVATION_URL": "api/v1/account/activation/{uid}/{token}/",
    "PASSWORD_RESET_CONFIRM_URL": "api/v1/account/reset-password-confirm/{uid}/{token}/",
    "PASSWORD_RESET_CONFIRM_RETYPE": True,
    "SET_PASSWORD_RETYPE": True,
    "SEND_ACTIVATION_EMAIL": True,
    "SEND_CONFIRMATION_EMAIL": True,
    "EMAIL": {
        "activation": "djoser.email.ActivationEmail",
    },
    "SERIALIZERS": {
        "user_create": USER_SERIALIZER,
        "current_user": USER_SERIALIZER,
        "user": USER_SERIALIZER,
        "user_list": "api.v1.users.serializers.UserShortInfoSerializer",
        "user_delete": USER_SERIALIZER,
    },
    "PERMISSIONS": {
        "user": (IS_USER_OWNER_OR_ADMIN_SERIALIZER,),
        "user_list": ("rest_framework.permissions.AllowAny",),
    },
}
