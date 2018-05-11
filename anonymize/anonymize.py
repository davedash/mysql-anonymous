#!/usr/bin/env python
from __future__ import print_function
import itertools
import logging
import random


log = logging.getLogger('anonymize')
common_hash_secret = "%016x" % (random.getrandbits(128))

listify = lambda x: x if isinstance(x, list) else [x]


class AnonymizeBaseAction(list):

    def __init__(self, scheme):
        self._scheme = scheme
        self.create()


class AnonymizeTruncate(AnonymizeBaseAction):

    def create(self):
        for truncate in self._scheme.database.get("truncate", []):
            self.append('TRUNCATE `{}`'.format(truncate))


class AnonymizeDelete(AnonymizeBaseAction):

    def create(self):
        for table, data in self._scheme.tables.iteritems():
            if 'delete' in data:
                self.append('DELETE FROM `{}` WHERE '.format(table) + ' AND '.join(
                    ['`{}` = "{}"'.format(f, v) for f, v in data['delete'].iteritems()]
                ))


class AnonymizeUpdate(AnonymizeBaseAction):

    def create(self):
        global common_hash_secret

        for table, data in self._scheme.tables.iteritems():
            updates = []
            for operation, details in data.iteritems():

                # tables columns
                if operation == 'nullify':
                    for field in listify(details):
                        updates.append("`%s` = NULL" % field)
                elif operation == 'random_int':
                    for field in listify(details):
                        updates.append("`%s` = ROUND(RAND()*1000000)" % field)
                elif operation == 'random_ip':
                    for field in listify(details):
                        updates.append("`%s` = INET_NTOA(RAND()*1000000000)" % field)
                elif operation == 'random_email':
                    for field in listify(details):
                        updates.append("`%s` = CONCAT(id, '@example.com')" % field)
                elif operation == 'random_username':
                    for field in listify(details):
                        updates.append("`%s` = CONCAT('_user_', id)" % field)
                elif operation == 'hash_value':
                    for field in listify(details):
                        updates.append("`%(field)s` = MD5(CONCAT(@common_hash_secret, `%(field)s`))"
                                       % dict(field=field))
                elif operation == 'hash_email':
                    for field in listify(details):
                        QUERY = "`%(field)s` = CONCAT(MD5(CONCAT(@common_hash_secret, `%(field)s`)), '@example.com')"
                        updates.append(QUERY % dict(field=field))
                elif operation == 'delete':
                    continue
                else:
                    log.warning('Unknown operation.')
            if updates:
                self.append('UPDATE `%s` SET %s' % (table, ', '.join(updates)))


class AnonymizeScheme(object):

    def __init__(self, name, cfg):
        self._name = name
        self._cfg = cfg

    def create(self):
        if self._print_use():
            print("USE `{}`".format(self.name))
        print("SET FOREIGN_KEY_CHECKS=0;")

        for action in self._actions():
            print("{};".format(action))
        print("SET FOREIGN_KEY_CHECKS=1;")
        print()

    @property
    def database(self):
        return self._cfg

    @property
    def tables(self):
        return self.database.get("tables", {})

    def _print_use(self):
        return "name" in self.database

    @property
    def name(self):
        return self.database['name'] or self._name

    def _actions(self):
        return itertools.chain(
            AnonymizeTruncate(self), AnonymizeDelete(self), AnonymizeUpdate(self))


class AnonymizeSchemes(object):

    def __init__(self, cfg):
        self._cfg = cfg
        self._print_use = False

    def build(self):
        print("--")
        print("SET @common_hash_secret=rand();")
        print("")

        for name, cfg in self._databases().items():
            if self._print_use:
                print("USE `{}`;".format(name))
            a = AnonymizeScheme(name, cfg)
            a.create()

    def _databases(self):
        if "databases" in self._cfg:
            self._print_use = True
            return self._cfg.get("databases")
        return {"default": self._cfg.get("database")}
