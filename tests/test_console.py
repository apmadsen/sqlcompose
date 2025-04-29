# pyright: basic
from unittest import TestCase, main
from sqlcompose import loads, load
from os import path
from subprocess import call
from sys import executable

class Test(TestCase):

    def test_existing_file_by_path(self):
        result = call(f"{executable} -m sqlcompose tests/main-query.sql")
        self.assertEqual(result, 0)

    def test_sql(self):
        result = call(f"""{executable} -m sqlcompose "SELECT * FROM $INCLUDE(tests/main-query.sql)" """)
        self.assertEqual(result, 0)


if __name__ == '__main__':
    main()

