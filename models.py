from helpers import cd_to_datetime, datetime_to_str
import pickle as pkl
import functools


class BuildError(UnboundLocalError):
    def __init__(self, msg):
        print(msg)


class NearEarthObject:
    def __init__(self, info):
        
        for key, value in info.items():
            if key == 'name':
                self.name = value if value else None
            elif key == 'diameter':
                if value:
                    self.diameter = float(value) 
                else:
                    self.diameter = float('nan')
            elif key == 'pha':
                self.hazardous = True if value == 'Y' else False
            elif key == 'pdes':
                self.designation = value
            else:
                pass
        
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
        return f"A NearEarthObject, {self.fullname}, has a diameter of {round(self.diameter, 3)} km and {self.hazard_msg}."

    def __repr__(self):
        return (f"NearEarthObject(designation={self.designation!r}, name={self.name!r}, diameter={self.diameter:.3f}, hazardous={self.hazardous!r})")


class CloseApproach:
    def __init__(self, info):
        for key, value in info.items():
            if key == 'cd':
                self.time = cd_to_datetime(value)
            elif key == 'dist':
                self.distance = float(value)
            elif key == 'v_rel':
                self.velocity = float(value)
            elif key == 'des':
                self._designation = value
            else:
                pass

        self.neo = None

    @property
    def time_str(self):
        return datetime_to_str(self.time)

    def __str__(self):
        return f"At {self.time_str}, {self.neo.fullname} approaches Earth at a distance of {round(self.distance, 2)} au and a velocity of {round(self.velocity, 2)} km/s."

    def __repr__(self):
        return (f"At CloseApproach(time={self.time_str!r},"
                f"distance={self.distance:.2f}, "
                f"velocity={self.velocity:.2f}, neo={self.neo!r})")
