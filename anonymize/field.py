# coding: utf-8
import logging
logger = logging.getLogger('anonymize')


class Field(object):

    def __init__(self, field, primary_key="id"):
        self._field = field
        self._primary_key = primary_key

    def render(self):
        return self.sql_field.format(
            field=self._field, primary_key=self._primary_key)


class Nullify(Field):
    sql_field = "`{field}` = NULL"


class RandomInt(Field):
    sql_field = "`{field}` = ROUND(RAND()*1000000)"


class RandomIp(Field):
    sql_field = "`{field}` = INET_NTOA(RAND()*1000000000)"


class RandomEmail(Field):
    sql_field = "`{field}` = CONCAT({primary_key}, '@example.com')"


class RandomUsername(Field):
    sql_field = "`{field}` = CONCAT('_user_', {primary_key})"


class RandomCellPhone(Field):
    sql_field = "`{field}` = LPAD({primary_key}, 13, 5)"


class RandomPhone(Field):
    sql_field = "`{field}` = LPAD({primary_key}, 12, 5)"


class RandomCpf(Field):
    sql_field = "`{field}` = LPAD({primary_key}, 11, 5)"


class RandomCnpj(Field):
    sql_field = "`{field}` = LPAD({primary_key}, 14, 5)"


class HashValue(Field):
    sql_field = "`{field}` = MD5(CONCAT(@common_hash_secret, `{field}`))"


class HashEmail(Field):
    sql_field = "`{field}` = CONCAT(MD5(CONCAT(@common_hash_secret, `{field}`)), '@example.com')"


class LoremIpsum(Field):
    sql_field = """`{field}` = `Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum`"""


class AnonymizeField(object):

    def __init__(self, data, primary_key):
        self._data = data
        self._primary_key = primary_key

        self._fields = {
            "nullify": Nullify,
            "random_int": RandomInt,
            "random_ip": RandomIp,
            "random_email": RandomEmail,
            "random_username": RandomUsername,
            "random_cell_phone": RandomCellPhone,
            "random_phone": RandomPhone,
            "random_cpf": RandomCpf,
            "random_cnpj": RandomCnpj,
            "hash_value": HashValue,
            "hash_email": HashEmail,
            'text_lorem_ipsum': LoremIpsum
        }

    def build(self):
        for operation, details in self._data.items():
            if self._valid_operation(operation):
                for field in self._listify(details):
                    yield self.get_field(operation, field)
            else:
                logger.warning("Unknown {} operation.".format(operation))

    def _valid_operation(self, operation):
        return operation in self._fields

    def _delete_operation(self, operation):
        return operation == "delete"

    def _listify(self, values):
        if isinstance(values, list):
            return values
        return [values, ]

    def get_field(self, operation, field):
        return self._fields[operation](field, self._primary_key)
