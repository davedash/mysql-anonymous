.SILENT:
PIP=.venv/bin/pip
PYTEST=.venv/bin/pytest
PYTHON=.venv/bin/python
COVERALLS=.venv/bin/coveralls


test:clean
	PYTHONPATH=anonymize ${PYTEST} -s -v --cov=anonymize --cov-report term-missing tests/${path}

venv:
	virtualenv .venv --python=python3

setup:venv
	${PIP} install -U pip
	${PIP} install -r requirements_dev.txt

clean:
	find . -name "*.pyc" -exec rm -rf {} \;

sample:
	PYTHONPATH=anonymize ${PYTHON} anonymize/__init__.py

coveralls:
	${COVERALLS}
