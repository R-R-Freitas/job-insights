from functools import lru_cache
import csv


@lru_cache
def read(path):
    """Reads a file from a given path and returns its contents

    Parameters
    ----------
    path : str
        Full path to file

    Returns
    -------
    list
        List of rows as dicts
    """
    with open(path, mode='r') as file:
        file_reader = csv.reader(file, delimiter=',', quotechar='"')
        header, *data = file_reader
        results = []
        for row in range(0, len(data)):
            line = {}
            for column in range(0, len(header)):
                line[header[column]] = data[row][column]
            results.append(line)
    return results
