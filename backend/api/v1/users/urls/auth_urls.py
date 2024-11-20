from django.urls import path

from api.v1.users.viewsets import LoginViewSet, LogoutViewSet, RegisterViewSet

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
