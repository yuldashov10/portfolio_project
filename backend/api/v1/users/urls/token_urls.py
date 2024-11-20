from django.urls import path

from api.v1.users.viewsets import TokenRefreshViewSet, TokenVerifyViewSet

token_patterns = [
    path(
        "refresh/",
        TokenRefreshViewSet.as_view(),
        name="token_refresh",
    ),
    path(
        "verify/",
        TokenVerifyViewSet.as_view(),
        name="token_verify",
    ),
]
