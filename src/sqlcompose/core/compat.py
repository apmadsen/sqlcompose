from os import path, sep
from re import compile

RX_FILE = compile(r"^[\w,\s-]+\.[A-Za-z]{3}$")
WINDOWS_PATH_SEP = "\\"
UNIX_PATH_SEP = "/"

def fix_path(file_path: str) -> str:
    """Replaces all path separators, be they Linux or Windows style
    to the standard path separator of the system.

    Args:
        file_path (str): The file path to fix.
    """
    for str in [ WINDOWS_PATH_SEP, UNIX_PATH_SEP ]:
        if str != path.sep:
            file_path = file_path.replace(str, path.sep)

    return file_path

def get_relative_path(file_path: str, root: str) -> str:
    """Get the path relative to root path.

    Args:
        file_path (str): The path.
        root (str): The root path.

    Returns:
        str: The relative path.
    """
    if root == file_path:
        return file_path
    else:
        return path.relpath(file_path, path.commonprefix([root, file_path]))

def is_file(text: str) -> bool:
    if path.isfile(text):
        return True
    elif sep in text and is_file(path.basename(text)):
        return True
    elif RX_FILE.match(text):
        return True

    return False
