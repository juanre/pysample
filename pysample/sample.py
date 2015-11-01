# -*- coding: utf-8 -*-
"""The docstring for the file.

A short summary of what it is about.
"""
from __future__ import division

import numpy as np
from pkg_resources import resource_filename, resource_string


def read_resource(resname):
    """Returns a resource found in the directory specified by the
    package_data parameter of the setup function in setup.py.

    >>> np.all(read_resource('res/diagonal.npy') == [[0., 1., 1.],
    ...                                              [1., 0., 1.],
    ...                                              [1., 1., 0.]])
    True
    >>> read_resource('res/hithere.txt').strip() == 'Hi there.'
    True

    """
    import os.path
    if os.path.splitext(resname)[1] == '.npy':
        return np.load(resource_filename(__name__, resname))
    return resource_string(__name__, resname)


def _doctest():
    import doctest
    doctest.testmod()


def main():
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)

    # https://docs.python.org/3.3/howto/argparse.html
    parser.add_argument('-t', '--test', help='run tests', action="store_true")
    parser.add_argument('-n', '--number', help='a number', type=int)
    parser.add_argument('astring', help='a positional (mandatory) argument')
    args = parser.parse_args()
    if args.test:
        _doctest()
    else:
        print args.astring


if __name__ == '__main__':
    main()
