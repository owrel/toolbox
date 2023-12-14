
__all__ = ["extract_filename"]

from os import PathLike
import re


def extract_filename(path: PathLike):
    x = 0
    y = len(path)
    if '/' in path:
        x = path.rindex('/') + 1

    if (m := re.search(r"\..*", path)):
        y = m.span()[0]

    return path[x:y]
