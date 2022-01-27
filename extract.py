"""
The file extracting data from .csv and .json files.

The main module calls these functions with the arguments provided at the
command line, and uses the resulting collections to build an `NEODatabase`.
"""
import csv
import json

from models import NearEarthObject, CloseApproach


def load_neos(path="data/neos.csv"):
    """Extract data from .csv file."""
    with open(path, 'r') as infile:
        reader = csv.DictReader(infile)
        collection = []
        for row in reader:
            collection.append(NearEarthObject(row['pdes'], row['name'],
                                              row['diameter'], row['pha']))
    return collection


def load_approaches(path='data/cad.json'):
    """Extract data from .json file."""
    with open(path, 'r') as infile:
        data = json.load(infile)['data']
        collection = []
        for i in data:
            collection.append(CloseApproach(i[0], i[3], i[4], i[7]))
    return collection
