## Mysql Anonymous

Contributors can benefit from having real data when they are
developing.  This script can do a few things (see `anonymize.yml`):

* Truncate any tables (logs, and other cruft which may have sensitive data)
* Nullify fields (emails, passwords, etc)
* Fill in random/arbitrary data:
    * Random integers
    * Random IP addresses
    * Email addresses
    * Usernames
    * Random string
* Set a fixed data
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

### YAML structure

#### Single database

Here's a commented example of a YAML file usable with `anonymize.py` to operate
upon a single database:

    database:

        # Delete all content from the tables named in the list below
        truncate:
            - list_of_table_names
            - from_which
            - to_remove_all_content

        tables:

            # Multiple tables can be named, with anonymizing handlers listed within
            table_name_1:
                nullify: [ more_columns, listed_here ]

            table_name_2:

                delete:
                    # Delete any rows where the column "column_name" contains 0
                    column_name: 0

                # Precise the primary key field, used for somes operations
                pk: pk_field

                # Set a variable
                # Ex : set a variable code with TO_TEST
                set_var_code: TO_TEST

                # Use a variable
                # Ex : set some fields with the variable code
                use_var_code: [status]
                # result => status field will take 'TO_TEST' value

                # Anonymize data with _field_{id}. You must have pk operation
                anonymize: [fieldA, fieldB]
                #result (for the PK = 1) => _fieldA_1 , _fieldB_1

                # Randomize data with some parameters
                # random_<type>_<length>. Ex : random_ALPHAnum_12 will randomize a 12 length string with ALPHA caps and numbers
                # type availables :
                #    alpha = 'abcedefghijklmnopqrstuvwyz'
                #    alphanum = 'abcedefghijklmnopqrstuvwyz0123456789'
                #    ALPHA = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
                #    ALPHAnum = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
                #    ALpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcedefghijklmnopqrstuvwyz'
                #    ALphanum = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcedefghijklmnopqrstuvwyz0123456789'
                random_alphanum_15: [some, fields]

                # Randomize data with md5
                # md5_<length>. Ex : md5_16 will randomize a 16 length string the md5 of a random string. You must have pk operation
                md5_16: [some, fields]

                # Change the named columns to NULL values
                nullify: [ column_names, to_blank_out ]

                # Fill the named columns with random integers
                random_int: [ columns, to_fill, with_random_numbers ]

                # Fill the named columns with random IP-address values
                random_ip: [ columns_to_fill, with_random_ip_addresses ]

                # Fill the named columns with random email-like values
                random_email: [ list, of, column, names ]

                # Fill the named columns with random alpha-numeric values
                random_username: [ list, of, column, names ]

                # For the hash_* handlers, column values are hashed along with
                # a random "secret" chosen at the start of the SQL. This
                # "secret" is never revealed, and helps scramble values
                # consistently across databases.
                #
                # This can be handy for identifiers shared across databases
                # that are sharded or belong to different applications that have
                # to integrate in some way

                # MD5 hash of column value with the secret
                hash_value: [ even, more, names ]

                # MD5 hash of column value + @mozilla.com
                hash_email: [ still, more_column, names ]

#### Multiple databases

You can specify multiple databases to be included in one anonymizing SQL
output. The `USE {table name}` command will be included before each database's
stream of commands, though one random hash "secret" will be shared between
them.

    databases:

        name_of_database_1:
            truncate:
                - tables
                - to_truncate
            table_name_1:
                nullify: [ columns_to, nullify_values ]

        name_of_database_2:
            truncate:
                - tables
                - to_truncate
            table_name_1:
                random_int: [ columns_to, nullify_values ]