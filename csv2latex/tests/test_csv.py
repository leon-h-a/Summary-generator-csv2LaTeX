import unittest
from csv2latex.utils import csv
from pathlib import Path
import os


class TestCsv(unittest.TestCase):

    def test_get_csv_filepath(self):
        path = csv.get_csv_filepath()
        self.assertEqual(path, (Path.cwd() / "file.csv").as_uri())

        """
            Add another <filename>.csv file to this dir to test the exception raising
        or
            Remove all <filename>.csv files to this dir to test the exception raising
        """
        # with self.assertRaises(ValueError):
        #     csv.get_csv_filepath()

    def test_get_csv_filename(self):
        filepath = "somePath\\somefile.csv"

        filename = csv.get_csv_filename(filepath)
        self.assertEqual(filename, "somefile")


if __name__ == "__main__":
    unittest.main()
