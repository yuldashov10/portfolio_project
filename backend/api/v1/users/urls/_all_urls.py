from django.urls import include, path

from .account_urls import account_patterns
from .auth_urls import auth_patterns
from .token_urls import token_patterns
from .users_urls import users_patterns

__all__ = ["urlpatterns"]

urlpatterns = [
    path("", include(auth_patterns)),
    path("account/", include(account_patterns)),
    path("token/", include(token_patterns)),
    path("users/", include(users_patterns)),
]
