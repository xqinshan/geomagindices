#!/usr/bin/env python
"""
simple demo of retrieving common geomagnetic indices by date
"""

from .base import get_indices


def cli():
    from argparse import ArgumentParser

    p = ArgumentParser()
    p.add_argument("date", help="time of observation yyyy-mm-ddTHH:MM:ss")
    p.add_argument("-s", "--smoothdays", help="days to smooth observation for f107a", type=int)
    a = p.parse_args()

    inds = get_indices(a.date, a.smoothdays)

    print(inds)
