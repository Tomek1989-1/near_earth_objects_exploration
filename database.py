"""
A database encapsulating collections of NEOs and their close approaches.

A `NEODatabase` holds an interconnected data set of NEOs and close approaches.
It provides methods to fetch an NEO by primary designation or by name, as well
as a method to query the set of close approaches that match a collection of
user-specified criteria.

Under normal circumstances, the main module creates one NEODatabase from the
data on NEOs and close approaches extracted by `extract.load_neos` and
`extract.load_approaches`.
"""


class NEODatabase:
    """NEODatabase object definition."""

    def __init__(self, neos, approaches):
        """Instance object creation."""
        self._neos = neos
        self._approaches = approaches

        # dictionary of neos with designation as a key
        self.neo_dict_designation = {}
        for neo in neos:
            self.neo_dict_designation[neo.designation] = neo

        # dictionary of neos with name as a key
        self.neo_dict_name = {}
        for neo in neos:
            self.neo_dict_name[neo.name] = neo

        # assigning NEO to each approach and all approaches to each NEO
        for approach in approaches:
            approach.neo = self.neo_dict_designation[approach._designation]
            self.neo_dict_designation[approach._designation].approaches.\
                append(approach)

    def get_neo_by_designation(self, designation):
        """Find and return an NEO by its primary designation.

        If no match is found, return `None` instead.
        Each NEO in the data set has a unique primary designation, as a string.
        """
        neo = self.neo_dict_designation.get(designation, None)
        return neo

    def get_neo_by_name(self, name):
        """Find and return an NEO by its name.

        If no match is found, return `None` instead.
        Not every NEO in the data set has a name. No NEOs are associated with
        the empty string nor with the `None` singleton.
        """
        neo = self.neo_dict_name.get(name, None)
        return neo

    def query(self, filters):
        """Query close approaches to find those that match all filters.

        :param filters: A collection of filters capturing user-specified
        criteria.
        :return: A stream of matching `CloseApproach` objects.
        """
        for approach in self._approaches:
            if filters.some_date:
                if approach.time.date() == filters.some_date:
                    pass
                else:
                    continue
            if filters.startdate:
                if approach.time.date() >= filters.startdate:
                    pass
                else:
                    continue
            if filters.enddate:
                if approach.time.date() <= filters.enddate:
                    pass
                else:
                    continue
            if filters.distancemin:
                if approach.distance > filters.distancemin:
                    pass
                else:
                    continue
            if filters.distancemax:
                if approach.distance < filters.distancemax:
                    pass
                else:
                    continue
            if filters.velocitymin:
                if approach.velocity > filters.velocitymin:
                    pass
                else:
                    continue
            if filters.velocitymax:
                if approach.velocity < filters.velocitymax:
                    pass
                else:
                    continue
            if filters.diametermin:
                if approach.neo.diameter > filters.diametermin:
                    pass
                else:
                    continue
            if filters.diametermax:
                if approach.neo.diameter < filters.diametermax:
                    pass
                else:
                    continue
            if filters.ishazardous is not None:
                if approach.neo.hazardous == filters.ishazardous:
                    pass
                else:
                    continue
            yield approach
