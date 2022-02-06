import pytest


def calculate_vat(price, vat):
    return price * vat / 100


@pytest.mark.parametrize("a, b, expected", [(10, 23, 2.3)])
def test_calculate_vat(a, b, expected):
    assert calculate_vat(a, b) == expected


