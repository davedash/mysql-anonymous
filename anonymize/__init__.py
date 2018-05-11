#!/usr/bin/env python
from __future__ import absolute_import
import yaml
from optparse import OptionParser
from anonymize import AnonymizeSchemes


class Anonymize(object):

    def __init__(self, file_name="sample.yml"):
        self._file_name = file_name

    def run(self):
        with open(self._file_name) as handle:
            a = AnonymizeSchemes(yaml.load(handle))
            a.build()


def main():
    parser = OptionParser()
    parser.add_option('-y', '--yaml')
    parser.add_option('-s', '--sample', default=1)
    (options, args) = parser.parse_args()

    anonymize = Anonymize()
    anonymize.run()


if __name__ == "__main__":
    main()
