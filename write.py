
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
            line = {}
            line['datetime_utc'] = helpers.datetime_to_str(approach.time)
            line['distance_au'] = approach.distance
            line['velocity_km_s'] = approach.velocity
            line['designation'] = approach._designation
            line['name'] = approach.neo.fullname
            line['diameter_km'] = approach.neo.diameter
            line['potentially_hazardous'] = approach.neo.hazardous
            writer.writerow(line)


def write_to_json(results, filename):
    output = []
    for approach in results:
        item = {'datetime_utc': approach.time_str,
                'distance_au': approach.distance,
                'velocity_km_s': approach.velocity,
                'neo': {'designation': approach._designation,
                       'name': approach.neo.name,
                       'diameter_km': approach.neo.diameter,
                       'potentially_hazardous': approach.neo.hazardous
                        }
               }
        output.append(item)
    with open(filename, 'w') as outfile:
        json.dump(output, outfile)