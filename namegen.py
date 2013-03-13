#!/usr/bin/env python
"""
Generate plausible names and email addresses, choosing names and
email domains with random choice weighted by requency.

No guarantees that combinations of names and emails will be unique.

Usage:

    >>> names = NameGen()
    >>> names.next()
    'Rhiannon Bland rbland1130@hotmail.co.uk'

"""

import os
import numpy as np

class NameGen():
    def __init__(self, weirdOrder=True):
        "Read data files and compute weights"
        self.data = {}
        for thing in ["girls", "boys", "lasts", "domains"]:
            self.data[thing] = {}
            self.data[thing]['items'] = self._getData(thing, weirdOrder)
            self.data[thing]['weights'] = self._getWeights(self.data[thing]['items'])

    def _getData(self, thing, weirdOrder=True):
        "Load data for thing"
        filepath = os.path.join("data", thing+".txt")
        data = [line.strip() for line in open(filepath).readlines()
                    if not line.startswith('#')]
        if weirdOrder:
            return list(reversed(data))
        return(data)

    def _getWeights(self, items):
        "Simply use cumulative sum as a means of assigning weight"
        return np.cumsum([i[0] for i in enumerate(items)])

    def _getWeightedRandom(self, thing):
        "Pick a thing, leaning toward the more common names over the less"
        throw = np.random.rand() * self.data[thing]['weights'][-1]
        index = np.searchsorted(self.data[thing]['weights'], throw)
        return self.data[thing]['items'][index]

    def _emailify(self, first, last):
        "Make an emaily kind of username for the given first and last names"
        first = first.lower()
        last = last.lower()
        eight = first[0] + last[:7]
        random = str(int(np.random.rand()*10000))
        return np.random.choice([
            eight,
            eight + random,
            first + random,
            ''.join([first, last]),
            '-'.join([first, last]),
            '.'.join([first, last]),
            ''.join([first[0], last]),
            ''.join([first[0], last, random]),
            '.'.join([first, last + random]),
            ''.join([first, last, random])
        ])

    def __iter__(self):
        return self

    def next(self):
        "Get a name and email address"
        first = self._getWeightedRandom(np.random.choice(['girls', 'boys']))
        last = self._getWeightedRandom('lasts')
        email = self._emailify(first, last)
        domain = self._getWeightedRandom('domains')
        return ' '.join([first, last, email+'@'+domain])

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        n = int(sys.argv[-1])
    else:
        n = 1

    names = NameGen()
    print '\n'.join([names.next() for i in range(n)])
