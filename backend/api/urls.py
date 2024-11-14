from django.conf import settings
from django.urls import include, path
from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view

from . import apps

schema_view = get_schema_view(title=settings.API_TITLE)

app_name = apps.ApiConfig.name

urlpatterns = [
    path("v1/", include("api.v1.urls")),
    path("docs/", include_docs_urls(title=settings.API_TITLE)),
    path("schema/", schema_view),
]
