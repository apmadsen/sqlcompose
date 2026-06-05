# ruff: noqa
# pyright: basic
from pytest import fixture, raises as assert_raises

from sqlcompose import loads, load, CircularDependencyError, FileNotFoundErr
from sqlcompose.core.functions import compose


def test_nonexisting():
    with assert_raises(FileNotFoundErr):
        load("nonexisting.sql")
    with assert_raises(FileNotFoundErr):
        load("tests/non_existing_include.sql")
    with assert_raises(FileNotFoundErr):
        compose("select * from $INCLUDE(some_file_that_does_not_exist.sql)", "SQL", ".", ".")


    filename = "tests/existing_include.sql"
    with open(filename, "r", encoding="utf-8") as file:
        with assert_raises(FileNotFoundErr):
            compose(file.read(), filename, filename, ".")

def test_reuse_composition():
    result = compose("select * from $INCLUDE(tests/includes/included-query3.sql)", "SQL", ".", ".")
    # print(result)
    assert len(result) > 0


def test_existing_file_by_path():
    result = load("tests/main-query.sql")
    # print(result)
    assert len(result) > 0

def test_sql():
    result = loads("SELECT * FROM $INCLUDE(tests/main-query.sql)")
    # print(result)
    assert len(result) > 0

def test_circular_dependency():
    with assert_raises(CircularDependencyError):
        load("tests/circular_left.sql")

