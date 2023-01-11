import sys
import pytest
try:
    from StringIO import StringIO
except:
    from io import StringIO


@pytest.fixture
def stdout():
    old_stdout = sys.stdout

    result = StringIO()
    sys.stdout = result
    return old_stdout, result
