import pytest
from .playground import contains_duplicate_approach1, contains_duplicate_approach2

@pytest.mark.parametrize("nums, expected", [
    ([1, 2, 3, 3], True),
    ([1, 2, 3, 4], False),
])
def test_contains_duplicate(nums, expected):
    assert contains_duplicate_approach1(nums) == expected
    assert contains_duplicate_approach2(nums) == expected


