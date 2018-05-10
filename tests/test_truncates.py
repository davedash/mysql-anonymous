from anonymize.anonymize import get_truncates


def test_should_get_the_empty_list():
    truncates = get_truncates({})

    assert truncates == []


def test_should_get_the_list_of_truncate_tables():
    truncates = get_truncates({
        "database": {
            "truncate": [
                "user",
                "subscribers"
            ]
        }
    })

    assert truncates == ['TRUNCATE `user`', 'TRUNCATE `subscribers`']
