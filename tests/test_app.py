# ruff: noqa
# pyright: basic
from os import path
from pytest import fixture, raises as assert_raises

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
