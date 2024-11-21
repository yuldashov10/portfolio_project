from django.urls import include, path, re_path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

from . import apps

app_name = apps.ApiConfig.name

urlpatterns = [
    re_path(r"^(?P<version>v1)/", include("api.v1.urls")),
    path(
        "schema/",
        SpectacularAPIView.as_view(api_version="v1"),
        name="schema",
    ),
    path(
        "docs/redoc/",
        SpectacularRedocView.as_view(
            url_name=f"{app_name}:schema",
        ),
        name="redoc",
    ),
    path(
        "docs/swagger/",
        SpectacularSwaggerView.as_view(
            url_name=f"{app_name}:schema",
        ),
        name="swagger-ui",
    ),
]
