PIP=.venv/bin/pip
PYTEST=.venv/bin/pytest

test:clean
	PYTHONPATH=. ${PYTEST} -s -v tests/${path}

venv:
	virtualenv .venv

setup:venv
	${PIP} install -U pip
	${PIP} install -r requirements_dev.txt

clean:
	find . -name "*.pyc" -exec rm -rf {} \;
