from __future__ import print_function
import itertools
import random
from field import AnonymizeField
from collections import OrderedDict


common_hash_secret = "%016x" % (random.getrandbits(128))


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
        for table, data in self._scheme.tables.items():
            if 'delete' in data:
                self.append('DELETE FROM `{}` WHERE '.format(table) + ' AND '.join(
                    ['`{}` = "{}"'.format(f, v) for f, v in data['delete'].items()]
                ))


class AnonymizeUpdate(AnonymizeBaseAction):

    def create(self):
        global common_hash_secret

        for table, data in self._scheme.tables.items():
            updates = []
            primary_key, exception = data.pop('primary_key', "id"), data.pop('exception', [])
            data = OrderedDict(sorted(data.items(), key=lambda t: t[0]))

            anon = AnonymizeField(data, primary_key)

            for n in anon.build():
                updates.append(n.render())

            if updates:
                self.append(
                    'UPDATE `{}` SET {}{}'.format(
                        table,
                        ', '.join(updates),
                        self._sql_exception(primary_key, exception)))

    def _sql_exception(self, primary_key, exception):
        where = ""
        if exception:
            where = " WHERE {primary_key} NOT IN({ids})".format(
                primary_key=primary_key, ids=", ".join(map(str, exception)))
        return where


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
