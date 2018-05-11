from anonymize.anonymize import get_updates


def test_should_get_the_update_list():
    data = get_updates({
        "database": {
            "tables": {
                "user": {
                    "nullify": ["phone", ],
                    "random_email": ["email", ],
                    "random_ip": ['ip']
                }
            }
        }
    })

    r = ["UPDATE `user` SET `phone` = NULL, `ip` = INET_NTOA(RAND()*1000000000), `email` = CONCAT(id, '@example.com')"]
    assert data == r
