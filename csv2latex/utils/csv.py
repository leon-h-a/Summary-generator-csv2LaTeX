import os
import re
import csv
from pathlib import Path
from csv2latex.models.textBlock import TextBlock


def get_csv_filepath():
    csv_files = list()
    all_files = os.listdir(Path("input_file"))

    for file in all_files:
        if ".csv" in file:
            csv_files.append(file)
        else:
            pass

    if len(csv_files) > 1:
        raise ValueError("There is more than one .csv file inside this directory. Leave only one .csv file!")

    elif len(csv_files) == 0:
        raise ValueError("There are no .csv files inside current directory.")

    else:
        return Path.cwd() / "input_file" / csv_files[0]


def get_csv_filename(filepath):
    matches = re.search("([a-zA-Z0-9\_\.\-\+\ ]+).csv$", str(filepath))
    return matches.group(1)


# todo: test this!
def _create_text_box(block):
    if len(block) <= 2:
        block.append("paragraph")

    obj = TextBlock(
        text=block[0],
        page=block[1],
        style=block[2]
    )
    return obj


def parse_csv(filepath):
    list_of_block_objects = list()

    with open(str(filepath)) as csvfile:
        filtered = (line.replace('\r', '') for line in csvfile)
        highlighted_blocks = csv.reader(filtered, delimiter=",")
        for block in highlighted_blocks:
            list_of_block_objects.append(
                _create_text_box(block)
            )

    return list_of_block_objects
