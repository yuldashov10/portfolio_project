from rest_framework_simplejwt.views import TokenBlacklistView

__all__ = ["LogoutViewSet"]


class LogoutViewSet(TokenBlacklistView):
    pass
