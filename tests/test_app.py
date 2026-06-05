# ruff: noqa
# pyright: basic
from os import path, chdir, curdir
from sys import stdin
from io import StringIO
from pytest import fixture, raises as assert_raises
from pytest_mock import MockerFixture

from sqlcompose.core.app import app


def test_missing_args():
    _result, code = app([])
    assert code == 2

def test_existing_file_by_path():
    result, code = app([path.join("tests", "main-query.sql")])
    assert len(result) > 0
    assert code == 0

def test_missing_file_by_path():
    result, code = app([path.join("tests", "nonexisting.sql")])
    assert len(result) > 0
    assert code == 3

    result, code = app([f"SELECT * FROM $INCLUDE({path.join('tests', 'nonexisting.sql')})"])
    assert len(result) > 0
    assert code == 3


def test_sql():
    result, code = app([f"SELECT * FROM $INCLUDE({path.join('tests', 'main-query.sql')})"])
    assert len(result) > 0
    assert code == 0

def test_pipe(mocker: MockerFixture):
    chdir("tests")
    try:
        with open("main-query.sql", "rt", encoding="utf8") as input:
            mocker.patch(f"sys.stdin", input)
            try:
                result, code = app([])
                assert len(result) > 0
                assert code == 0
            finally:
                mocker.resetall()
    finally:
        chdir("..")