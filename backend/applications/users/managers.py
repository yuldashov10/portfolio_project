from typing import Any

from django.contrib.auth.models import BaseUserManager
from django.utils.text import gettext_lazy as _


class UserManager(BaseUserManager):
    """
    Custom manager for the User model.

    This manager provides methods to create regular users and
    superusers, with built-in validation for required fields.
    """

    __SUPERUSER_REQUIRED_FIELDS: dict[str, bool] = {
        "is_staff": True,
        "is_superuser": True,
        "is_active": True,
        "is_admin": True,
        "is_moder": True,
        "is_vip": True,
        "is_blocked": False,
    }

    def create_user(
        self,
        username: str,
        email: str,
        password: str,
        **extra_fields: dict[str, Any],
    ):
        """
        Create and return a regular user
        with the given username, email, and password.

        :param username: The username for the user.
        :param email: The email address for the user.
        :param password: The password for the user.
        :param extra_fields: Additional fields to set on the user model.
        :return: The created User instance.
        :raises ValueError: If the username or email is not provided.
        """
        self._validate_username(username)
        self._validate_email(email)

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            **extra_fields,
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(
        self,
        username: str,
        email: str,
        password: str,
        **extra_fields: dict[str, Any],
    ):
        """
        Create and return a superuser
        with the given username, email, and password.

        :param username: The username for the superuser.
        :param email: The email address for the superuser.
        :param password: The password for the superuser.
        :param extra_fields: Additional fields to set on the superuser model.
        :return: The created User instance.
        :raises ValueError: If any required fields are not set to True.
        """
        self.__set_superuser_required_fields(**extra_fields)
        self._validate_superuser_required_fields(**extra_fields)

        return self.create_user(username, email, password, **extra_fields)

    def _validate_superuser_required_fields(
        self,
        **extra_fields: dict[str, Any],
    ) -> None:
        """
        Validate the fields required for creating a superuser.

        :param extra_fields: Extra fields to be validated.
        :raises ValueError: If any required fields are not set to True.
        """

        for (
            field,
            value,
        ) in self.__get_required_fields_for_superuser().items():
            if extra_fields.get(field) is not value:
                raise ValueError(_(f"Superuser must have {field}={value}."))

    def _validate_username(self, username: str) -> None:
        """
        Validate the username provided.

        :param username: The username for the user.
        :raises ValueError: If the username is not provided.
        """
        if not username:
            raise ValueError(_("The username must be set"))

    def _validate_email(self, email: str) -> None:
        """
        Validate the email address provided.

        :param email: The email address for the user.
        :raises ValueError: If the email is not provided.
        """
        if not email:
            raise ValueError(_("The email must be set"))

    @classmethod
    def __get_required_fields_for_superuser(cls) -> dict[str, bool]:
        """
        Returns the required fields for a superuser with their default values.

        This method is used internally to validate and set fields
        specific to the superuser when creating a new user.

        :return: A dictionary of field names and their expected values.
        """
        return cls.__SUPERUSER_REQUIRED_FIELDS

    def __set_superuser_required_fields(
        self, **extra_fields: dict[str, Any]
    ) -> None:
        """
        Set default fields for the superuser.

        :param extra_fields: Extra fields to be set on the user model.
        """
        for (
            field,
            default_value,
        ) in self.__get_required_fields_for_superuser().items():
            extra_fields.setdefault(field, default_value)
