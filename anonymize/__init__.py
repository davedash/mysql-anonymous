#!/usr/bin/env python
from __future__ import absolute_import
from optparse import OptionParser


class Anonymize(object):
    pass


def main():
    parser = OptionParser()
    parser.add_option('-y', '--yaml')
    parser.add_option('-s', '--sample', default=1)
    (options, args) = parser.parse_args()

    anonymize = Anonymize()
    anonymize.run()


if __name__ == "__main__":
    main()
