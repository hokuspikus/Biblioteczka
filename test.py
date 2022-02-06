import pytest

from functions import div


@pytest.mark.parametrize("a, b, expected", [
    (6, 3, 2),
    (7.5, 2.5, 3.0),
    ('6', '3', 2),
])
def test_div(a, b, expected):
    assert div(a, b) == expected


def test_div_by_0():
    with pytest.raises(ZeroDivisionError):
        div(2, 0)


