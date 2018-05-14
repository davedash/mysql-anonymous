import os
import sys
import pytest
try:
    from StringIO import StringIO
except:
    from io import StringIO
from anonymize import Anonymize


@pytest.fixture
def sample():
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    return os.path.join(BASE_DIR, 'anonymize', "sample1.yml")


@pytest.fixture
def stdout():
    old_stdout = sys.stdout

    result = StringIO()
    sys.stdout = result
    return old_stdout, result


def test_should_get_trucate_at_output(sample, stdout):
    a = Anonymize(file_name=sample, sample="")
    a.run()

    sys.stdout, result = stdout
    assert "TRUNCATE `stats_collections_counts`;" in result.getvalue()
