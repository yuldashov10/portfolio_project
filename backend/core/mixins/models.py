from django.db import models
from django.utils.text import gettext_lazy as _


class VerboseNamesMixin:
    """Устанавливает кастомные описания для указанных полей модели."""

    @classmethod
    def __validate(cls, **validate_data) -> None:
        invalid_fields: list[str] = [
            field_name
            for field_name, text in validate_data.items()
            if not hasattr(cls, field_name)
        ]

        if invalid_fields:
            raise AttributeError(
                _(
                    f"{cls.__class__.__name__} "
                    f"не имеет поле(й) {invalid_fields}"
                )
            )

    @classmethod
    def set_verbose_names(cls, **kwargs) -> None:
        cls.__validate(**kwargs)

        for field_name, text in kwargs.items():
            cls._meta.get_field(field_name).verbose_name = _(text)


class CreatedAtAndUpdatedAtMixin(models.Model):
    """Устаналивает поля `created_at` и `updated_at` для модели."""

    created_at = models.DateTimeField(
        _("Дата создания"),
        auto_now=True,
    )
    updated_at = models.DateTimeField(
        _("Дата обновления"),
        auto_now_add=True,
    )

    class Meta:
        abstract = True
