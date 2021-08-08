import unittest
from csv2latex.utils import csv
from pathlib import Path


class TestCsv(unittest.TestCase):

    def get_csv_file(self):
        filepath = csv.get_csv_file(".")
        self.assertEqual(str(filepath), str(Path("testfile.csv")))

        """
            Add another <filename>.csv file to './input_file' dir to test the exception raising
        or
            Remove all <filename>.csv files to './input_file' dir to test the exception raising
        
        with self.assertRaises(ValueError):
            csv.get_csv_filepath()
        """

    def test_get_csv_filename(self):
        filepath = "someDrive/somePath/somsefile.csv"

        filename = csv.get_csv_excaped_filename(filepath)
        self.assertEqual(filename, "somsefile")

    # todo: test "csv._remove_newlines"


if __name__ == "__main__":
    unittest.main()
