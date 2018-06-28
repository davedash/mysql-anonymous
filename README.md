## Mysql Anonymous

[![Build Status](https://travis-ci.org/riquellopes/mysql-anonymous.svg?branch=master)](https://travis-ci.org/riquellopes/mysql-anonymous)
[![Coverage Status](https://coveralls.io/repos/github/riquellopes/mysql-anonymous/badge.svg?branch=master)](https://coveralls.io/github/riquellopes/mysql-anonymous?branch=master)

Contributors can benefit from having real data when they are
developing.  This script can do a few things (see `sample1.yml` or `sample2.yml`):

* Truncate any tables (logs, and other cruft which may have sensitive data)
* Nullify fields (emails, passwords, etc)
* Fill in random/arbitrary data:
    * Random integers
    * Random IP addresses
    * Random Cell Phone
    * Random Phone
    * Random [CPF](https://pt.wikipedia.org/wiki/Cadastro_de_pessoas_f%C3%ADsicas)
    * Random [CNPJ](https://pt.wikipedia.org/wiki/Cadastro_Nacional_da_Pessoa_Jur%C3%ADdica)
    * Email addresses
    * Usernames
* Delete rows based on simple rules:  e.g.
  ``DELETE FROM mytable WHERE private = "Yes"``:

   ```yml
    database:
        tables:
            mytable:
                nullify:
                    private: Yes
    ```

* Apply rules exception in some cases: e.g.
  ``UPDATE mytable SET cellphone=NULL WHERE id NOT IN(556, 889)``:

  ```yml
  database:
      tables:
          mytable:
              exception:
               - 556
               - 889
              nullify:
               - cellphone
  ```

* Define an other name for primary key of table: e.g.
  ``UPDATE mytable SET `email` = CONCAT(user_id, '@example.com')``:

  ```yml
  database:
      tables:
          primary_key: user_id
          mytable:
              random_email: email
  ```

Installation
------------
```sh
pip install https://github.com/riquellopes/mysql-anonymous/tarball/master
```
CookBook
--------
```sh
    anonymize --sample-one
    anonymize --sample-two
    anonymize -y database.yml
```
