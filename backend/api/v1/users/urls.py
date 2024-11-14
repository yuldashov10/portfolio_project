from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenBlacklistView,
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from api.v1.users.viewsets import UserViewSet

router = DefaultRouter()

router.register(r"users", UserViewSet, basename="users")

auth_patterns = [
    path(
        "jwt/refresh/",
        TokenRefreshView.as_view(),
        name="token_refresh",
    ),
    path(
        "jwt/verify/",
        TokenVerifyView.as_view(),
        name="token_verify",
    ),
]

urlpatterns = [
    path("", include(router.urls)),
    path(
        "register/",
        UserViewSet.as_view({"post": "create"}),
        name="register",
    ),
    # TODO: Make custom method "activate"
    path(
        "activation/<str:uid>/<str:token>/",
        UserViewSet.as_view({"post": "activation"}),
        name="activation",
    ),
    path(
        "login/",
        TokenObtainPairView.as_view(),
        name="login",
    ),
    path(
        "logout/",
        TokenBlacklistView.as_view(),
        name="token_blacklist",
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
    path("auth/", include(auth_patterns)),
]
