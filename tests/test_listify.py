from anonymize.anonymize import listify


def test_should_get_a_list_item():
    assert listify("") == [""]


def test_should_get_a_list_none():
    assert listify(None) == [None, ]
