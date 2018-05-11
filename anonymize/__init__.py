#!/usr/bin/env python
import os
import yaml
from optparse import OptionParser
from anonymize import AnonymizeSchemes


class Anonymize(object):

    def __init__(self, file_name, sample):
        self._file_name = file_name
        self._sample = sample

    def run(self):
        with open(self.file_name) as handle:
            a = AnonymizeSchemes(yaml.load(handle))
            a.build()

    @property
    def file_name(self):
        if self._sample:
            BASE_DIR = os.path.dirname(os.path.dirname(
                os.path.dirname(os.path.dirname(__file__))))
            return os.path.join(
                BASE_DIR, 'anonymize', "sample{}.yml".format(self._sample))
        return self._file_name


def main():
    parser = OptionParser()
    parser.add_option('-y', '--yaml')
    parser.add_option('-s', '--sample', default=1)
    (options, __) = parser.parse_args()

    anonymize = Anonymize(**{
        "file_name": options.yaml,
        "sample": options.sample
    })
    anonymize.run()


if __name__ == "__main__":
    main()
