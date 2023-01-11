import sys
from anonymize.anonymize import AnonymizeScheme, AnonymizeSchemes


def test_property_print_use_should_get_true():
    s = AnonymizeScheme("anything", {
        "name": {}
    })

    assert s._print_use()


def test_property_print_use_should_get_false():
    s = AnonymizeScheme("anything", {
        "names": {}
    })

    assert s._print_use() is False


def test_should_start_with_the_correct_header(stdout):
    s = AnonymizeScheme("anything", {
        "name": {}
    })

    s.create()
    sys.stdout, result = stdout

    assert "USE `anything`\nSET FOREIGN_KEY_CHECKS=0;\nSET FOREIGN_KEY_CHECKS=1;\n\n" in result.getvalue()


def test_shoulg_get_true_and_empty_dict():
    s = AnonymizeSchemes({
        "databases": {}
    })

    databases = s._databases()

    assert s._print_use
    assert databases == {}
