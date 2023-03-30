import pytest
from main import string_to_map, most_common


@pytest.fixture
def words():
    return {
        "foo": 3,
        "bar": 1,
        "baz": 5,
        "quux": 2,
    }


@pytest.fixture
def text():
    return """
    foo
    foo
        bar
    foo
            baz
            baz
                quux
    foo
    """


def test_string_to_map(text):
    assert string_to_map(text) == {
        "foo": 4,
        "bar": 1,
        "baz": 2,
        "quux": 1,
    }


@pytest.mark.parametrize("n, expected", [
    (2, ["baz=5", "foo=3"]),
    (3, ["baz=5", "foo=3", "quux=2"]),
    (4, ["baz=5", "foo=3", "quux=2", "bar=1"]),
])
def test_most_frequent(words, n, expected):
    assert most_common(words, n) == expected
