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


def test_should_get_the_update_list_with_lipsum():
    data = AnonymizeUpdate(AnonymizeScheme("default", {
        "tables": {
            "user": {
                "text_lorem_ipsum": ["text", ],
            }
        }
    }))

    r = ["UPDATE `user` SET `text` = `Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum`"]

    assert data == r
