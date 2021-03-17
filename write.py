
import csv
import json
from models import NearEarthObject
import helpers


def write_to_csv(results, filename):
    fieldnames = ('datetime_utc', 'distance_au', 'velocity_km_s', 'designation', 'name', 'diameter_km', 'potentially_hazardous')
    with open(filename, 'w') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for approach in results:
            neo = NearEarthObject(pdes=approach._designation)
            line = {}
            line['datetime_utc'] = helpers.datetime_to_str(approach.time)
            line['distance_au'] = approach.distance
            line['velocity_km_s'] = approach.velocity
            line['designation'] = approach._designation
            line['name'] = neo.fullname
            line['diameter_km'] = neo.diameter
            line['potentially_hazardous'] = neo.hazardous
            writer.writerow(line)


def write_to_json(results, filename):
    approaches = list()
    for approach in results:
            neo = NearEarthObject(pdes=approach._designation)
            line = {}
            line['datetime_utc'] = helpers.datetime_to_str(approach.time)
            line['distance_au'] = approach.distance
            line['velocity_km_s'] = approach.velocity
            line['designation'] = approach._designation
            line['name'] = neo.fullname
            line['diameter_km'] = neo.diameter
            line['potentially_hazardous'] = neo.hazardous
            approaches.append(line)

    with open(filename, 'w') as f:
        writer = json.dump(approaches, f, indent=2)