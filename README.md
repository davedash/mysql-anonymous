## Mysql Anonymous

[![Build Status](https://travis-ci.org/riquellopes/mysql-anonymous.svg?branch=master)](https://travis-ci.org/riquellopes/mysql-anonymous)

Contributors can benefit from having real data when they are
developing.  This script can do a few things (see `anonymize.yml`):

* Truncate any tables (logs, and other cruft which may have sensitive data)
* Nullify fields (emails, passwords, etc)
* Fill in random/arbitrary data:
    * Random integers
    * Random IP addresses
    * Email addresses
    * Usernames
* Delete rows based on simple rules:  e.g.
  ``DELETE FROM mytable WHERE private = "Yes"``:

    database:
        tables:
            mytable:
                delete:
                    private: Yes

### Usage

    python anonymize.py > anon.sql
    cat anon.sql | mysql
