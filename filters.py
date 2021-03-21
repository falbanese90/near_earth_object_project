"""Create filter classes to parse and organize data."""
import operator


class UnsupportedCriterionError(NotImplementedError):
    """A filter criterion is unsupported."""


class AttributeFilter:
    """Creates class of attributes and uses them to filter database."""

    def __init__(self, op, value):
        """Filter attributes."""
        self.op = op
        self.value = value

    def __call__(self, approach):
        """Call the operator to compare values and filter."""
        return self.op(self.get(approach), self.value)

    @classmethod
    def get(cls, approach):
        """Retrieve specific value."""
        raise UnsupportedCriterionError

    def __repr__(self):
        """Machine readable format."""
        return (f"{self.__class__.__name__}"
                f"(op=operator.{self.op.__name__}"
                f", value={self.value})")


class DateFilter(AttributeFilter):
    """Date Attribute filter."""

    @classmethod
    def get(cls, approach):
        """Retrieve specific value."""
        return approach.time.date()


class DistanceFilter(AttributeFilter):
    """Distance attribute filter."""

    @classmethod
    def get(cls, approach):
        """Retrieve specific value."""
        return approach.distance


class VelocityFilter(AttributeFilter):
    """Velocity attribute filter."""

    @classmethod
    def get(cls, approach):
        """Retrieve specific value."""
        return approach.velocity


class DiameterFilter(AttributeFilter):
    """Diameter filter."""

    @classmethod
    def get(cls, approach):
        """Retrieve specific value."""
        return approach.neo.diameter


class HazardousFilter(AttributeFilter):
    """Hazardous filter."""

    @classmethod
    def get(cls, approach):
        """Retrieve specific value."""
        return approach.neo.hazardous


def create_filters(date=None, start_date=None, end_date=None,
                   distance_min=None, distance_max=None,
                   velocity_min=None, velocity_max=None,
                   diameter_min=None, diameter_max=None,
                   hazardous=None):
    """Create filters based on user input."""
    filters = list()

    if date is not None:
        filters.append(DateFilter(operator.eq, date))
    if start_date is not None:
        filters.append(DateFilter(operator.ge, start_date))
    if end_date is not None:
        filters.append(DateFilter(operator.le, end_date))
    if distance_min is not None:
        filters.append(DistanceFilter(operator.ge, distance_min))
    if distance_max is not None:
        filters.append(DistanceFilter(operator.le, distance_max))
    if velocity_min is not None:
        filters.append(VelocityFilter(operator.ge, velocity_min))
    if velocity_max is not None:
        filters.append(VelocityFilter(operator.le, velocity_max))
    if diameter_min is not None:
        filters.append(DiameterFilter(operator.ge, diameter_min))
    if diameter_max is not None:
        filters.append(DiameterFilter(operator.le, diameter_max))
    if hazardous is not None:
        filters.append(HazardousFilter(operator.eq, hazardous))

    return tuple(filters)


def limit(iterator, n=None):
    """Create a user specified limit."""
    for i, v in enumerate(iterator):
        yield v
        if i + 1 == n:
            break
