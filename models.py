"""Create indivual class objects for NEO and Aproaches."""
from helpers import cd_to_datetime, datetime_to_str
import pickle as pkl
import functools


class BuildError(UnboundLocalError):
    """Specified Error with message to user."""

    def __init__(self, msg):
        """Create action of object instance."""
        print(msg)


class NearEarthObject:
    """Unpack data retrieved by the extract function.

    Uses them to build a Near Earth Object.
    """

    def __init__(self, info):
        """Create NEO Attributes."""
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
        """Return a string based on hazardous boolean value."""
        if self.hazardous:
            return "is potentially hazardous"
        else:
            return "is not potentially hazardous"

    @property
    def fullname(self):
        """Connect designation and name to return full name."""
        if self.name:
            return self.designation + ' ' + self.name
        else:
            return self.designation

    def __str__(self):
        """Return String representation of object."""
        return (f"A NearEarthObject, {self.fullname}, has a diameter"
                f"of {round(self.diameter, 3)} km and {self.hazard_msg}.")

    def __repr__(self):
        """Return Machine Readbale representation of object."""
        return (f"NearEarthObject(designation={self.designation!r},"
                f"name={self.name!r}," f"diameter {self.diameter:.3f},"
                f"hazardous={self.hazardous!r})")


class CloseApproach:
    """Build the Close Approach Object."""

    def __init__(self, info):
        """Create Close Approach Attribute."""
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
        """Return string version of time attribute."""
        return datetime_to_str(self.time)

    def __str__(self):
        """Return String representation of object."""
        return (f"At {self.time_str}, {self.neo.fullname}"
                f"approaches Earth at a distance of {round(self.distance, 2)}"
                f"au and a velocity of {round(self.velocity, 2)} km/s.")

    def __repr__(self):
        """Return Machine Readbale representation of object."""
        return (f"At CloseApproach(time={self.time_str!r},"
                f"distance={self.distance:.2f}, "
                f"velocity={self.velocity:.2f}, neo={self.neo!r})")
