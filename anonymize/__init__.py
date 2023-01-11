#!/usr/bin/env python
# coding: utf-8
from __future__ import print_function, absolute_import
import os
import logging
from yaml import Loader, load
from optparse import OptionParser
from .anonymize import AnonymizeSchemes

logging.basicConfig(
    filename='anonymize.log',
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.DEBUG)


class Anonymize(object):

    def __init__(self, file_name, sample):
        self._file_name = file_name
        self._sample = sample
        self._run = True

        self.validate()

    def run(self):
        if self._run:
            with open(self.file_name) as handle:
                a = AnonymizeSchemes(load(handle, Loader=Loader))
                a.build()

    @property
    def file_name(self):
        if self.is_sample():
            return os.path.join(
                os.path.dirname(os.path.dirname(__file__)),
                'anonymize',
                "sample{}.yml".format(self._sample))
        return self._file_name

    def is_sample(self):
        return self._file_name is None and self._sample

    def validate(self):
        if self._sample is None and self._file_name is None:
            self._run = False
            print('\033[91m' + "Invalid option.")


def main():
    parser = OptionParser()
    parser.add_option('-y', '--yaml', help="YAML file to read data from.")
    parser.add_option('--sample-one', const=1, action="store_const")
    parser.add_option('--sample-two', const=2, action="store_const")

    (options, __) = parser.parse_args()

    anonymize = Anonymize(**{
        "file_name": options.yaml,
        "sample": options.sample_one or options.sample_two
    })
    anonymize.run()


if __name__ == "__main__":
    main()
