## Mysql Anonymous

[![Build Status](https://travis-ci.org/riquellopes/mysql-anonymous.svg?branch=master)](https://travis-ci.org/riquellopes/mysql-anonymous)

Contributors can benefit from having real data when they are
developing.  This script can do a few things (see `anonymize.yml`):

* Truncate any tables (logs, and other cruft which may have sensitive data)
* Nullify fields (emails, passwords, etc)
* Fill in random/arbitrary data:
    * Random integers
    * Random IP addresses
    * Random Cell Phone
    * Random Phone
    * Random [CPF](https://pt.wikipedia.org/wiki/Cadastro_de_pessoas_f%C3%ADsicas)
    * Email addresses
    * Usernames
* Delete rows based on simple rules:  e.g.
  ``DELETE FROM mytable WHERE private = "Yes"``:

    database:
        tables:
            mytable:
                delete:
                    private: Yes

#### Installation
```sh
pip install https://github.com/riquellopes/mysql-anonymous/tarball/master
```
### CookBook
```sh
    anonymize --sample-one
    anonymize --sample-two
    anonymize -y database.yml
```
