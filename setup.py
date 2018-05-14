"""
    Contributors can benefit from having real data when they are developing. This script can do a few things (see anonymize.yml):

    Truncate any tables (logs, and other cruft which may have sensitive data)

    Nullify fields (emails, passwords, etc)

    Fill in random/arbitrary data:

    Random integers
    Random IP addresses
    Email addresses
    Usernames
    Delete rows based on simple rules: e.g. DELETE FROM mytable WHERE private = "Yes":

    database: tables: mytable: delete: private: Yes
"""

from setuptools import setup

setup_params = {
    "entry_points": {
        "console_scripts": [
            "anonymize=anonymize:main"
        ]
    }
}


setup(
    author="Dave Dash",
    author_email="dd+github@davedash.com, contato@henriquelopes.com.br",
    version='0.2',
    name="Mysql Anonymous",
    url="https://github.com/davedash/mysql-anonymous",
    packages=["anonymize"],
    platforms=['python >= 2.7'],
    description=__doc__,
    long_description=__doc__,
    install_requires=["pyyaml"],
    py_modules=["anonymize"],
    package_data={'': ['sample1.yml', 'sample2.yml']},
    include_package_data=True,
    **setup_params
)
