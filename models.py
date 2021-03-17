from helpers import cd_to_datetime, datetime_to_str
from class_builder import get_neo, get_neo_attr, get_cad_attr, cad
import pickle as pkl
import functools


class BuildError(UnboundLocalError):
    def __init__(self, msg):
        print(msg)


class NearEarthObject:
    def __init__(self, name=None, pdes=None):
        if name:
            carrier = get_neo_attr(get_neo(name=name))
        if pdes:
            carrier = get_neo_attr(get_neo(pdes=pdes))
        if not name and not pdes:
            raise BuildError('Please supply pdes or name.')
        # Here we use the dictionary of neo to update all of self atributes.
        self.__dict__.update(carrier)
        # Create an empty initial collection of linked approaches.
        self.approaches = []

    @property
    def hazard_msg(self):
        if self.hazardous:
            return "is potentially hazardous"
        else:
            return "is not potentially hazardous"

    @property
    def fullname(self):
        if self.name:
            return self.designation + ' ' + self.name
        else:
            return self.designation

    def __str__(self):
        return f"A NearEarthObject, {self.fullname}, has a diameter of"
        f"{round(self.diameter, 3)} km and {self.hazard_msg}."

    def __repr__(self):
        return (f"NearEarthObject(designation={self.designation!r},"
                f"name={self.name!r}, "
                f"diameter={self.diameter:.3f}, hazardous={self.hazardous!r})")


class CloseApproach:
    def __init__(self, attr):
        self.__dict__.update(attr)
        self.neo = None

    @property
    def time_str(self):
        return datetime_to_str(self.time)

    def __str__(self):
        """Return `str(self)`."""
        return f"At {self.time_str}, {self.neo} approaches"
        f"Earth at a distance of {round(self.distance, 2)} au and a velocity"
        f"of {round(self.velocity, 2)} km/s."

    def __repr__(self):
        return (f"At CloseApproach(time={self.time_str!r},"
                f"distance={self.distance:.2f}, "
                f"velocity={self.velocity:.2f}, neo={self.neo!r})")
