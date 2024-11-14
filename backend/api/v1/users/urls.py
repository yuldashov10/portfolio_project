from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.v1.users.viewsets import (
    LoginViewSet,
    LogoutViewSet,
    RegisterViewSet,
    TokenRefreshViewSet,
    TokenVerifyViewSet,
    UserViewSet,
)

router = DefaultRouter()

router.register(r"users", UserViewSet, basename="users")

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

auth_patterns = [
    path(
        "register/",
        RegisterViewSet.as_view({"post": "create"}),
        name="register",
    ),
    path(
        "login/",
        LoginViewSet.as_view(),
        name="login",
    ),
    path(
        "logout/",
        LogoutViewSet.as_view(),
        name="logout",
    ),
]

account_patterns = [
    # TODO: Make custom method "activate"
    path(
        "activation/<str:uid>/<str:token>/",
        UserViewSet.as_view({"post": "activation"}),
        name="activation",
    ),
    path(
        "resend-activation/",
        UserViewSet.as_view({"post": "resend_activation"}),
        name="resend_activation",
    ),
    path(
        "reset-password/",
        UserViewSet.as_view({"post": "reset_password"}),
        name="reset_password",
    ),
    path(
        "reset-password-confirm/<str:uid>/<str:token>/",
        UserViewSet.as_view({"post": "reset_password_confirm"}),
        name="reset_password_confirm",
    ),
]

urlpatterns = [
    path("", include(router.urls)),
    path("", include(auth_patterns)),
    path("account/", include(account_patterns)),
    path("token/", include(token_patterns)),
]
