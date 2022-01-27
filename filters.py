"""Provide filters for querying close approaches & limit the generated results.

The `create_filters` function produces a collection of objects that is used by
the `query` method to generate a stream of `CloseApproach` objects that match
all of the desired criteria. The arguments to `create_filters` are provided by
the main module and originate from the user's command-line options.

The `limit` function simply limits the maximum number of values produced by an
iterator.

"""
import itertools


class create_filters:
    """Create object to filter NEO's close approaches."""

    def __init__(self, date=None, start_date=None, end_date=None,
                 distance_min=None, distance_max=None,
                 velocity_min=None, velocity_max=None,
                 diameter_min=None, diameter_max=None,
                 hazardous=None):
        """Create filter object."""
        self.some_date = date
        self.startdate = start_date
        self.enddate = end_date
        self.distancemin = distance_min
        self.distancemax = distance_max
        self.velocitymin = velocity_min
        self.velocitymax = velocity_max
        self.diametermin = diameter_min
        self.diametermax = diameter_max
        self.ishazardous = hazardous


def limit(iterator, n=None):
    """Produce a limited stream of values from an iterator.

    If `n` is 0 or None, don't limit the iterator at all.
    """
    if not n:
        return iterator
    else:
        return itertools.islice(iterator, n)
