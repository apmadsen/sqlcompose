
class FileNotFoundErr(Exception):
    __slots__ = [ "__filename" ]

    def __init__(self, filename: str, error: str | None = None):
        super().__init__(error or f"File {filename} not found")
        self.__filename = filename

    @property
    def filename(self) -> str:
        return self.__filename # pragma: no cover