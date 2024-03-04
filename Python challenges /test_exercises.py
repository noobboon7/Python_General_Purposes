import pytest
from miles_to_kilometers import convert_miles_to_kilometers
def TestMileCovertion():
    assert convert_miles_to_kilometers(4) == 6.43738
    assert convert_miles_to_kilometers(5) == 8.04672