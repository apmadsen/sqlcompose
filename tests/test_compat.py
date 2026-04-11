# ruff: noqa
# pyright: basic
from pytest import fixture, raises as assert_raises
from sys import platform

from sqlcompose.core.compat import fix_path, get_relative_path


def test_fix_path():
    if platform == "win32":
        tests = {
            "sql\\file.sql" : "sql\\file.sql",
            "sql\\file.sql" : "sql/file.sql",
        }
    else:
        tests = {
            "sql/file.sql" : "sql\\file.sql",
            "sql/file.sql" : "sql/file.sql",
        }

    for expected_result, file_path in tests.items():
        result = fix_path(file_path)
        assert result == expected_result


def test_get_relative_path():
    if platform == "win32":
        tests = {
            "sql\\file.sql" : ("sql\\file.sql", "sql\\file.sql"),
            "sql\\file.sql" : ("sql\\file.sql", "c:\\app\\"),
            "sql\\file.sql" : ("c:\\app\\sql\\file.sql", "c:\\app\\"),
        }

        p = "sql\\file.sql"
        assert p == get_relative_path(p, p)
    else:
        tests = {
            "sql/file.sql" : ("sql/file.sql", "sql/file.sql"),
            "sql/file.sql" : ("sql/file.sql", "/app/"),
            "sql/file.sql" : ("/app/sql/file.sql", "/app/"),
        }
        p = "sql/file.sql"
        assert p == get_relative_path(p, p)

    for expected_result, (file_path, root) in tests.items():
        result = get_relative_path(file_path, root)
        assert result == expected_result

