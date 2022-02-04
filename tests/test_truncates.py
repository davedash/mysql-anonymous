from anonymize.anonymize import AnonymizeTruncate, AnonymizeScheme


def test_should_get_the_empty_list():
    truncates = AnonymizeTruncate(AnonymizeScheme("default", {}))

    assert truncates == []


def test_should_get_the_list_of_truncate_tables():
    truncates = AnonymizeTruncate(AnonymizeScheme("default", {
        "truncate": [
            "user",
            "subscribers"
        ]
    }))

    assert truncates == ['TRUNCATE `user`', 'TRUNCATE `subscribers`']
