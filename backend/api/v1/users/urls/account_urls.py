from django.urls import path

from api.v1.users.viewsets import ActivateUserAccount, UserViewSet

account_patterns = [
    path(
        "activation/<str:uid>/<str:token>/",
        ActivateUserAccount.as_view({"post": "account_activation"}),
        name="account_activation",
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
