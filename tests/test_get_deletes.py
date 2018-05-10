from anonymize.anonymize import get_deletes


def test_should_get_the_empty_list():
    truncates = get_deletes({})

    assert truncates == []


def test_should_get_the_list_of_delete_itens():
    deleted = get_deletes({
        "database": {
            "tables": {
                "user": {
                    "delete": {"id": 1}
                }
            }
        }
    })

    assert deleted == ['DELETE FROM `user` WHERE `id` = "1"']
