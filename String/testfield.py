import pytest

from .dsa import is_palindrome_approch1, is_palindrome_approch2, is_palindrome_approch3
from .playground import (
    character_frequency_approach1,
    character_frequency_approach2,
    contains_duplicate_approach1,
    contains_duplicate_approach2,
    is_anagram_approach1,
    is_anagram_approach2,
)


@pytest.mark.parametrize(
    "string, expected", [("abhay", {"a": 2, "b": 1, "h": 1, "y": 1})]
)
def test_character_frequency(string, expected):
    print("\nTesting for character frequency..")
    assert character_frequency_approach1(string) == expected
    assert character_frequency_approach2(string) == expected
    print("Test Passed")


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 2, 3, 3], True),
        ([1, 2, 3, 4], False),
    ],
)
def test_contains_duplicate(nums, expected):
    print("Testing contains duplicate")
    assert contains_duplicate_approach1(nums) == expected
    assert contains_duplicate_approach2(nums) == expected
    print("Test Passed")


@pytest.mark.parametrize(
    "string1, string2, expected",
    [
        ("racecar", "carrace", True),
        ("jar", "jam", False),
    ],
)
def test_is_anagram(string1, string2, expected):
    print("Testing is anagram")
    assert is_anagram_approach1(string1, string2) == expected
    assert is_anagram_approach2(string1, string2) == expected
    print("Test Passed")


# DSA TestCases
@pytest.mark.parametrize(
    "string, expected",
    [
        ("madam", True),
        ("something", False),
        ("civic", True),
        ("Civic", True),
        ("abca", False),
        ("a123a456a", False),
    ],
)
def test_is_palindrome(string, expected):
    print("Testing is palindrome")
    assert is_palindrome_approch1(string) == expected
    assert is_palindrome_approch2(string) == expected
    assert is_palindrome_approch3(string) == expected
    print("Test Passed")
