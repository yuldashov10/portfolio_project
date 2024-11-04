from django.core.validators import RegexValidator
from django.utils.text import gettext_lazy as _


class TelegramURLValidator(RegexValidator):
    regex = r"^https:\/\/(?:www\.)t.me\/.*$"
    code = "invalid_url"
    message = _("Неправильный URL-адрес Telegram")
