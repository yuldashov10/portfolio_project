from typing import Any

USER_SERIALIZER: str = "api.v1.users.serializers.UserSerializer"

DJOSER: dict[str, Any] = {
    "LOGIN_FIELD": "username",
    "HIDE_USERS": False,
    "USER_CREATE_PASSWORD_RETYPE": True,
    "ACTIVATION_URL": "api/v1/activation/{uid}/{token}/",
    "PASSWORD_RESET_CONFIRM_URL": "api/v1/reset-password-confirm/{uid}/{token}/",
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
    },
    "PERMISSIONS": {
        "user": ("rest_framework.permissions.IsAuthenticatedOrReadOnly",),
        "user_list": ("rest_framework.permissions.AllowAny",),
    },
}
