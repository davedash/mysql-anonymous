from anonymize.anonymize import AnonymizeUpdate, AnonymizeScheme


def test_should_get_the_update_list():
    data = AnonymizeUpdate(AnonymizeScheme("default", {
        "tables": {
            "user": {
                "nullify": ["phone", ],
                "random_email": ["email", ],
                "random_ip": ['ip']
            }
        }
    }))

    r = ["UPDATE `user` SET `phone` = NULL, `ip` = INET_NTOA(RAND()*1000000000), `email` = CONCAT(id, '@example.com')"]
    assert data == r


def test_should_get_the_update_list_with_cnpj():
    data = AnonymizeUpdate(AnonymizeScheme("default", {
        "tables": {
            "user": {
                "nullify": ["phone", ],
                "random_cnpj": ["cnpj", ]
            }
        }
    }))

    r = ['UPDATE `user` SET `phone` = NULL, `cnpj` = LPAD(id, 14, 5)']
    assert data == r

