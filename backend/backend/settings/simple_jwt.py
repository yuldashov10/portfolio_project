from datetime import timedelta
from typing import Any

from decouple import config

SIMPLE_JWT: dict[str, Any] = {
    "ACCESS_TOKEN_LIFETIME": timedelta(
        minutes=config(
            "JWT_ACCESS_TOKEN_LIFETIME",
            cast=int,
        ),
    ),
    "REFRESH_TOKEN_LIFETIME": timedelta(
        days=config(
            "JWT_REFRESH_TOKEN_LIFETIME",
            cast=int,
        ),
    ),
    "SLIDING_TOKEN_LIFETIME": timedelta(
        minutes=config(
            "JWT_SLIDING_TOKEN_LIFETIME",
            cast=int,
        ),
    ),
    "SLIDING_TOKEN_REFRESH_LIFETIME": timedelta(
        days=config(
            "JWT_SLIDING_TOKEN_REFRESH_LIFETIME",
            cast=int,
        ),
    ),
    "SLIDING_TOKEN_REFRESH_EXP_CLAIM": config(
        "JWT_SLIDING_TOKEN_REFRESH_EXP_CLAIM",
        cast=str,
    ),
    "AUTH_HEADER_TYPES": (config("AUTH_HEADER_TYPES", cast=str),),
    "AUTH_TOKEN_CLASSES": (
        "rest_framework_simplejwt.tokens.AccessToken",
        "rest_framework_simplejwt.tokens.RefreshToken",
    ),
    "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
    "ALGORITHM": config("JWT_ALGORITHM", cast=str),
    "SIGNING_KEY": config("JWT_SINGING_KEY", cast=str),
    "UPDATE_LAST_LOGIN": config("JWT_UPDATE_LAST_LOGIN", cast=bool),
    "ROTATE_REFRESH_TOKENS": config("JWT_ROTATE_REFRESH_TOKENS", cast=bool),
    "BLACKLIST_AFTER_ROTATION": config(
        "JWT_BLACKLIST_AFTER_ROTATION",
        cast=bool,
    ),
}
