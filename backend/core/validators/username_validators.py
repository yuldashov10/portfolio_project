from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.utils.deconstruct import deconstructible
from django.utils.text import gettext_lazy as _


@deconstructible
class UsernameValidator(RegexValidator):
    """
    Validator for usernames with specific restrictions.

    This validator ensures that a username contains only lowercase
    letters, digits, and at most UNDERSCORES_MAX_COUNT underscores.
    """

    UNDERSCORES_MAX_COUNT: int = 2
    regex = r"^[a-z0-9_]{1,}[a-z0-9]$"
    message = _(
        "Enter a valid username. Only lowercase letters, digits, "
        f"and at most {UNDERSCORES_MAX_COUNT} underscores are allowed. "
        "Username must not end with an underscore."
    )

    def __call__(self, username) -> None:
        super().__call__(username)
        self.check_number_of_underscore(username)

    def check_number_of_underscore(self, username: str) -> None:
        if username.count("_") > self.UNDERSCORES_MAX_COUNT:
            raise ValidationError(
                _(
                    "Username can't contain more than "
                    f"{self.UNDERSCORES_MAX_COUNT} underscores."
                ),
                code="invalid_username",
            )


@deconstructible
class RestrictedUsernamesValidator:
    """
    Validator for checking for banned username.

    :param restricted_usernames: A dictionary of restricted usernames, where
    keys represent categories and values are lists of restricted names.
    """

    def __init__(
        self,
        restricted_usernames: dict[str, tuple[str, ...]],
    ) -> None:
        self.__restricted_usernames = restricted_usernames

    def __call__(self, username: str) -> None:
        self._validate_username(username)

    def _validate_username(self, username: str) -> None:
        """
        Checks that the username is not restricted.

        The check is case-insensitive.

        :param username: The username to validate.
        :raises ValidationError: If the username is restricted.
        """
        username = username.lower()
        for names in self.__restricted_usernames.values():
            if username in names:
                raise ValidationError(
                    _("This username is forbidden."),
                    code="forbidden_username",
                )
