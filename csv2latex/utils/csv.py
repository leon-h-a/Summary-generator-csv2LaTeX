import os
from pathlib import Path


def get_csv_filpath():
    csv_files = list()
    all_files = os.listdir()

    for file in all_files:
        if ".csv" in file:
            csv_files.append(file)
        else:
            pass

    if len(csv_files) > 1:
        raise Exception("There is more than one .csv file in side this directory.")

    else:
        return (Path.cwd() / csv_files[0]).as_uri()


def get_csv_filename():
    raise NotImplemented
