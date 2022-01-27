"""
This file contains definition of NEO and approach objects.

A `NearEarthObject` maintains a collection of its close approaches, and a
`CloseApproach` maintains a reference to its NEO.
"""
from helpers import cd_to_datetime, datetime_to_str


class NearEarthObject():
    """
    NEO object class.

    A `NearEarthObject` also maintains a collection of its close approaches -
    initialized to an empty collection, but eventually populated in the
    `NEODatabase` constructor.
    """

    def __init__(self, designation, name=None, diameter=None, pha=None):
        """NEO object instatation."""
        self.designation = str(designation)
        if name:
            self.name = str(name)
        else:
            self.name = None
        if diameter:
            self.diameter = float(diameter)
        else:
            self.diameter = float('nan')
        if pha == 'Y':
            self.hazardous = True
        else:
            self.hazardous = False
        self.approaches = []

    @property
    def fullname(self):
        """NEO's fullname attribute."""
        return f'{self.designation!r} ({self.name!r})'

    def __str__(self):
        """Define string representation of the object."""
        return f'A NearEarthObject: fullname={self.fullname}, diameter={self.diameter:.3f} km, hazardous={self.hazardous}'

    def __repr__(self):
        """Define representation to be returned."""
        return f'NearEarthObject: designation={self.designation!r}, name={self.name!r}, diameter={self.diameter:.3f}, hazardous={self.hazardous}'


class CloseApproach():
    """Close approach object class."""

    def __init__(self, designantion, time, distance, velocity):
        """Close approach object instatation."""
        self._designation = str(designantion)
        self.time = cd_to_datetime(time)
        self.distance = float(distance)
        self.velocity = float(velocity)

        # Attribute for the referenced NEO, originally None.
        self.neo = None

    @property
    def time_str(self):
        """Approach time in string format."""
        self.time_str_format = datetime_to_str(self.time)
        return self.time_str_format

    def __str__(self):
        """Define string representation of the object."""
        return f"On {self.time_str}, {self._designation} approaches Earth at a distance of {self.distance:.2f} au and velocity of {self.velocity:.2f} km/s"

    def __repr__(self):
        """Define representation to be returned."""
        return f"CloseApproach: designation={self._designation!r}, time={self.time_str}, distance={self.distance:.2f}, velocity={self.velocity:.2f}"
