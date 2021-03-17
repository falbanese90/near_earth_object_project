from extract import load_neos, load_approaches
from models import NearEarthObject, CloseApproach
from class_builder import get_neo, get_neo_attr, get_cad_attr
import helpers
import functools


# Creates a cache file to expedite searches
# and queries by storing results in dict.
def memoize(function):
    function._cache = {}

    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        key = (args, tuple(kwargs.items()))
        if key not in function._cache:
            function._cache[key] = function(*args, **kwargs)
            return function._cache[key]
        return function._cache[key]
    return wrapper


neos = load_neos()
approaches = load_approaches()


class NEODatabase:
    def __init__(self, neos=neos, approaches=approaches):
        self._neos = neos
        self._approaches = approaches

    @memoize
    def get_neo_by_designation(self, designation):
        neo = models.NearEarthObject(pdes=designation)
        for items in self._approaches:
            if items['des'] == neo.designation:
                cad_attr = {}
                cad_object = items
                cad_attr['time'] = helpers.cd_to_datetime(cad_object['cd'])
                cad_attr['distance'] = float(cad_object['dist'])
                cad_attr['velocity'] = float(cad_object['v_rel'])
                cad_attr['_designation'] = cad_object['des']
                approach = CloseApproach(cad_attr)
                approach.neo = neo.fullname
                neo.approaches.append(str(approach))
        return neo

    @memoize
    def get_neo_by_name(self, name):
        neo = NearEarthObject(name=name)
        for items in self._approaches:
            if items['des'] == neo.designation:
                cad_attr = {}
                cad_object = items
                cad_attr['time'] = helpers.cd_to_datetime(cad_object['cd'])
                cad_attr['distance'] = float(cad_object['dist'])
                cad_attr['velocity'] = float(cad_object['v_rel'])
                cad_attr['_designation'] = cad_object['des']
                approach = CloseApproach(cad_attr)
                approach.neo = neo.fullname
                neo.approaches.append(str(approach))

        return neo

    def query(self, filters=()):
        for item in self._approaches[::-1]:
            cad_attr = {}
            cad_object = item
            cad_attr['time'] = helpers.cd_to_datetime(cad_object['cd'])
            cad_attr['distance'] = float(cad_object['dist'])
            cad_attr['velocity'] = float(cad_object['v_rel'])
            cad_attr['_designation'] = cad_object['des']
            approach = CloseApproach(cad_attr)
            approach.neo = NearEarthObject(pdes=approach._designation)
            if all(map((lambda x: x.__call__(approach)), filters)):
                yield approach
