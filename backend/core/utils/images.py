import os
import uuid
from typing import Any

from django.utils.deconstruct import deconstructible


@deconstructible
class UploadAndRenameImage(object):
    """Renames the name of the upload image to uuid4."""

    def __init__(self, path: str) -> None:
        self.__sub_path: str = path

    def __call__(self, instance: Any, filename: str) -> str:
        extension: str = filename.split(".")[-1]
        new_filename: str = f"{uuid.uuid4().hex}.{extension}"

        return os.path.join(self.__sub_path, new_filename)
