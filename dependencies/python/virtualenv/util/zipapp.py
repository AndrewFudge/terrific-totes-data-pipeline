from __future__ import annotations  # noqa: A005

import logging
import os
import zipfile

from virtualenv.info import IS_WIN, ROOT

LOGGER = logging.getLogger(__name__)


def read(full_path):
    sub_file = _get_path_within_zip(full_path)
    with zipfile.ZipFile(ROOT, "r") as zip_file, zip_file.open(sub_file) as file_handler:
        return file_handler.read().decode("utf-8")


def extract(full_path, dest):
    LOGGER.debug("extract %s to %s", full_path, dest)
    sub_file = _get_path_within_zip(full_path)
    with zipfile.ZipFile(ROOT, "r") as zip_file:
        info = zip_file.getinfo(sub_file)
        info.filename = dest.name
        zip_file.extract(info, str(dest.parent))


def _get_path_within_zip(full_path):
    full_path = os.path.realpath(os.path.abspath(str(full_path)))
    prefix = f"{ROOT}{os.sep}"
    if not full_path.startswith(prefix):
        msg = f"full_path={full_path} should start with prefix={prefix}."
        raise RuntimeError(msg)
    sub_file = full_path[len(prefix) :]
    if IS_WIN:
        # paths are always UNIX separators, even on Windows, though __file__ still follows platform default
        sub_file = sub_file.replace(os.sep, "/")
    return sub_file


__all__ = [
    "extract",
    "read",
]
