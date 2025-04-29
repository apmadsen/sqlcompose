# pyright: basic
from unittest import TestCase, main
from sqlcompose import loads, load
from os import path
from subprocess import call
from sys import executable, platform

class Test(TestCase):

    quote = '"' if platform == "win32" else "'"

    def test_existing_file_by_path(self):
        result = call(f"{executable} -m sqlcompose tests/main-query.sql")
        self.assertEqual(result, 0)

    def test_sql_nonexisting(self):
        result = call(f"{executable} -m sqlcompose {self.quote}SELECT * FROM $INCLUDE(tests.sql){self.quote}")
        self.assertEqual(result, 1)

    def test_sql(self):
        result = call(f"{executable} -m sqlcompose {self.quote}SELECT * FROM $INCLUDE(tests/main-query.sql){self.quote}")

        self.assertEqual(result, 0)


if __name__ == '__main__':
    main()

