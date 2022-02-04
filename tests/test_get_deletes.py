from anonymize.anonymize import AnonymizeDelete, AnonymizeScheme


def test_should_get_the_empty_list():
    truncates = AnonymizeDelete(AnonymizeScheme("default", {}))

    assert truncates == []


def test_should_get_the_list_of_delete_itens():
    deleted = AnonymizeDelete(AnonymizeScheme("default", {
        "tables": {
            "user": {
                "delete": {"id": 1}
            }
        }
    }))

    assert deleted == ['DELETE FROM `user` WHERE `id` = "1"']
