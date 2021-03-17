
import csv
import json

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path='data/neos.csv'):

    neos = []
    with open(neo_csv_path) as f:
        reader = csv.DictReader(f)
        for elem in reader:
            neos.append(elem)
    return neos


def load_approaches(cad_json_path='data/cad.json'):
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

    return cad_dicts
