import pytest
from anonymize.field import AnonymizeField, Nullify


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
