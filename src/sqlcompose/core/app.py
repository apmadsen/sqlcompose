from argparse import ArgumentParser

from sqlcompose.core.functions import load, loads
from sqlcompose.core.compat import is_file
from sqlcompose.core.file_not_found_err import FileNotFoundErr


def app(args: list[str]) -> tuple[str, int]:
    try:
        parser = ArgumentParser(prog = "sqlcompose")
        parser.add_argument("input", type=str, help = "SQL expression or location of an SQL file")
        pargs = parser.parse_args(args)

        if is_file(pargs.input):
            sql = load(pargs.input)
        else:
            sql = loads(pargs.input)

        return sql, 0
    except SystemExit as ex:
        return str(ex), 2
    except (FileNotFoundErr, FileNotFoundError) as ex:
        return str(ex), 3
    except Exception as ex: # pragma: no cover
        return f"Unexpected error: {ex}", 1
