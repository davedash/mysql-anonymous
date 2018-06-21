import pytest
from anonymize.field import (
    AnonymizeField, Nullify, RandomCellPhone, RandomPhone, RandomCpf, RandomCnpj)


@pytest.fixture
def anon():
    return AnonymizeField({}, "id")


def test_should_get_a_list_item(anon):
    assert anon._listify("") == [""]


def test_should_get_a_list_none(anon):
    assert anon._listify(None) == [None, ]


def test_should_get_true(anon):
    assert anon._valid_operation("nullify")


def test_should_get_false(anon):
    assert anon._valid_operation("nullifys") is False


def test_should_get_true_for_delete_operations(anon):
    assert anon._delete_operation("delete")


def test_should_get_Nullify_instance(anon):
    assert isinstance(anon.get_field("nullify", "id"), Nullify)


def test_should_get_RandomCellPhone_instance(anon):
    cell_phone = anon.get_field("random_cell_phone", "id")
    assert isinstance(cell_phone, RandomCellPhone)
    assert cell_phone.render() == "`id` = LPAD(id, 13, 5)"


def test_should_get_RandomPhone_instance(anon):
    phone = anon.get_field("random_phone", "id")
    assert isinstance(phone, RandomPhone)
    assert phone.render() == "`id` = LPAD(id, 12, 5)"


def test_should_get_RandomCpf_instance(anon):
    cpf = anon.get_field("random_cpf", "id")
    assert isinstance(cpf, RandomCpf)
    assert cpf.render() == "`id` = LPAD(id, 11, 5)"

def test_should_get_RandomCnpj_instance(anon):
    cnpj = anon.get_field("random_cnpj", "cnpj")
    assert isinstance(cnpj, RandomCnpj)
    assert cnpj.render() == "`cnpj` = LPAD(id, 14, 5)"