import pytest
from miles_to_kilometers import convert_miles_to_kilometers


def test_conversion():
    assert convert_miles_to_kilometers(4) == 6.437376
    assert convert_miles_to_kilometers(5) == 8.04672