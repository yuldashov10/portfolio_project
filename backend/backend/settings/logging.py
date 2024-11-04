from typing import Any

VERSION: int = 1
LOGS_FILE_MAX_SIZE_BYTES: int = 1024 * 1024 * 5
LOGS_FILE_BACKUP_COUNT: int = 5

LOGGING: dict[str, Any] = {
    "version": VERSION,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "{asctime} {levelname} {filename} {funcName} {lineno} {message}",
            "style": "{",
        },
        "simple": {
            "format": "{asctime} {levelname} - {message}",
            "style": "{",
        },
    },
    "filters": {
        "require_debug_false": {
            "()": "django.utils.log.RequireDebugFalse",
        },
        "require_debug_true": {
            "()": "django.utils.log.RequireDebugTrue",
        },
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "filters": ["require_debug_true"],
            "formatter": "simple",
        },
        "log_file": {
            "level": "DEBUG",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": "api.log",
            "maxBytes": LOGS_FILE_MAX_SIZE_BYTES,
            "backupCount": LOGS_FILE_BACKUP_COUNT,
            "formatter": "verbose",
        },
        "error_file": {
            "level": "ERROR",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": "api_error.log",
            "maxBytes": LOGS_FILE_MAX_SIZE_BYTES,
            "backupCount": LOGS_FILE_BACKUP_COUNT,
            "formatter": "verbose",
        },
        "mail_admins": {
            "level": "ERROR",
            "class": "django.utils.log.AdminEmailHandler",
            "filters": ["require_debug_false"],
            "formatter": "verbose",
        },
    },
    "loggers": {
        "portfolio_project_api": {
            "handlers": ["console", "log_file", "error_file", "mail_admins"],
            "level": "DEBUG",
        },
        "django.request": {
            "handlers": ["mail_admins", "error_file"],
            "level": "ERROR",
            "propagate": False,
        },
    },
}
