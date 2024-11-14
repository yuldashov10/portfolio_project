from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

__all__ = ["TokenRefreshViewSet", "TokenVerifyViewSet"]


class TokenRefreshViewSet(TokenRefreshView):
    pass


class TokenVerifyViewSet(TokenVerifyView):
    pass
