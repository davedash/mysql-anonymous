from anonymize.anonymize import get_deletes


def test_should_get_the_empty_list():
    truncates = get_deletes({})

    assert truncates == []
