"""Extract Data and creates object classes."""
from models import CloseApproach, NearEarthObject
import csv
import json
import pickle as pkl


def load_neos(neo_csv_path='data/neos.csv'):
    """Load neos and unpack them in order to build objects."""
    neos_csv = []
    with open(neo_csv_path) as f:
        reader = csv.DictReader(f)
        for elem in reader:
            neos_csv.append(elem)
    neos = []
    for neo in neos_csv:
        n = NearEarthObject(neo)
        neos.append(n)
    return neos


def load_approaches(cad_json_path='data/cad.json'):
    """Load cloase approaches and unpack them in order to build objects."""
    with open(cad_json_path) as f:
        cad = json.load(f)
    # I further organized this json object by creating a dictionary to map
    # field names to each value.
    fields = cad['fields']
    cad_dicts = []
    for object in cad['data']:
        section = {}
        x = 0
        for label in fields:
            section[label] = object[x]
            x += 1
        cad_dicts.append(section)
    approaches = []
    with open('neo_dicts.pkl', 'rb') as f:
        neo_dicts = pkl.load(f)
    for approach in cad_dicts:
        a = CloseApproach(approach)
        neo = neo_dicts.get(a._designation, None)
        a.neo = neo
        approaches.append(a)
    return approaches
