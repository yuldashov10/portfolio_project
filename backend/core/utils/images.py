import os
from uuid import uuid4

from django.utils.deconstruct import deconstructible


@deconstructible
class UploadAndRenameImage(object):
    """Переименует название загруженного изображения в uuid4."""

    def __init__(self, path) -> None:
        self.__sub_path = path

    def __call__(self, instance, filename) -> str:
        ext: str = filename.split(".")[-1]
        filename: str = f"{uuid4().hex}.{ext}"

        return os.path.join(self.__sub_path, filename)
