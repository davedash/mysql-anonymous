import os
import sys
import pytest
from anonymize import Anonymize


@pytest.fixture
def sample():
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    return os.path.join(BASE_DIR, 'anonymize', "sample1.yml")


def test_should_get_trucate_at_output(sample, stdout):
    a = Anonymize(file_name=sample, sample="")
    a.run()

    sys.stdout, result = stdout
    assert "TRUNCATE `stats_collections_counts`;" in result.getvalue()
    assert " WHERE id NOT IN(556, 889)" in result.getvalue()
