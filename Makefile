PIP=.venv/bin/pip
PYTEST=.venv/bin/pytest
PYTHON=.venv/bin/python

test:clean
	PYTHONPATH=anonymize ${PYTEST} -s -v tests/${path}

venv:
	virtualenv .venv

setup:venv
	${PIP} install -U pip
	${PIP} install -r requirements_dev.txt

clean:
	find . -name "*.pyc" -exec rm -rf {} \;

sample:
	PYTHONPATH=anonymize ${PYTHON} anonymize/__init__.py
