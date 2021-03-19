from extract import load_neos, load_approaches
from models import NearEarthObject, CloseApproach
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


# query_list = []
# for item in approaches:
#     if item.distance >= .08 and item.distance <= .33:
#         query_list.append(item)


class NEODatabase:
    def __init__(self, neos, approaches):
        self._neos = neos
        self._approaches = approaches
        
        self.designation_neo_dict = {}
        self.name_neo_dict = {}
        
        for neo in self._neos:
            self.designation_neo_dict[neo.designation] = neo
            if neo.name:
                self.name_neo_dict[neo.name] = neo
                
        for approach in self._approaches:
            neo = self.designation_neo_dict[approach._designation]
            approach.neo = neo
            neo.approaches.append(approach)



    @memoize
    def get_neo_by_designation(self, designation):
        neo = self.designation_neo_dict.get(designation, None)
        return neo

    @memoize
    def get_neo_by_name(self, name):
        neo = self.name_neo_dict.get(name, None)
        return neo

    def query(self, filters=()):
        for approach in self._approaches:
            if all(map((lambda x: x.__call__(approach)), filters)):
                yield approach
