# pyright: basic
from unittest import TestCase, main
from sqlcompose import loads, load
from os import path


class Test(TestCase):
    def test_nonexisting(self):
        self.assertRaises(FileNotFoundError, load, "nonexisting.sql")

    def test_existing_file_by_path(self):
        result = load("tests/main-query.sql")
        # print(result)
        self.assertTrue(len(result) > 0)

    def test_sql(self):
        result = loads("SELECT * FROM $INCLUDE(tests/main-query.sql)")
        # print(result)
        self.assertTrue(len(result) > 0)


if __name__ == '__main__':
    main()

