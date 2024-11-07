from pathlib import Path

from decouple import Csv, config
from django.core.management.utils import get_random_secret_key

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = config("SECRET_KEY", default=get_random_secret_key(), cast=str)
DEBUG = config("DEBUG", default=False, cast=bool)
ALLOWED_HOSTS = config("ALLOWED_HOSTS", cast=Csv())

ROOT_URLCONF = "backend.urls"
WSGI_APPLICATION = "backend.wsgi.application"

LANGUAGE_CODE = "en-UK"
TIME_ZONE = "Europe/Moscow"
USE_I18N = True
USE_TZ = True

MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "media/"
STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "static/"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# https://github.com/adamchainz/django-cors-headers#configuration
CORS_ALLOWED_ORIGINS = config("CORS_ALLOWED_ORIGINS", cast=Csv())
CSRF_TRUSTED_ORIGINS = config("CSRF_TRUSTED_ORIGINS", cast=Csv())


API_TITLE = "Portfolio API"
API_DESCRIPTION = ""

AUTH_USER_MODEL = "users.User"
