import pytest

from .dsa import (
    atoi_approch_1,
    atoi_approch_2,
    check_rotation_approach1,
    check_rotation_approach2,
    check_rotation_using_kmp,
    encrypt_the_string,
    equal_point_in_brackets_approach1,
    equal_point_in_brackets_approach2,
    check_anagram_approach1,
    first_non_repeating_character_approach1,
    first_non_repeating_character_approach2,
    is_palindrome_approach1,
    is_palindrome_approach2,
    is_palindrome_approach3,
    is_palindrome_approach4,
    reverse_string_approach1,
    reverse_string_approach2,
    reverse_string_approach3,
    roman_to_integer,
)
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
    assert is_palindrome_approach1(string) == expected
    assert is_palindrome_approach2(string) == expected
    assert is_palindrome_approach3(string) == expected
    assert is_palindrome_approach4(string) == expected
    print("Test Passed")


@pytest.mark.parametrize(
    "string, expected",
    [("abcd", "dcba"), ("Abcd", "dcbA")],
)
def test_reverse_string(string, expected):
    print("Testing reverse of string")
    assert reverse_string_approach1(string) == expected
    assert reverse_string_approach2(string) == expected
    assert reverse_string_approach3(string) == expected
    print("Test passed !")


@pytest.mark.parametrize(
    "string1, string2, expected",
    [
        ("aab", "aba", True),
        ("abcd", "acbd", False),
        ("abcd", "cdab", True),
        ("ab", "abcd", False),
    ],
)
def test_check_rotation(string1, string2, expected):
    print("Testing check rotation")
    assert check_rotation_approach1(string1, string2) == expected
    assert check_rotation_approach2(string1, string2) == expected
    assert check_rotation_using_kmp(string1, string2) == expected
    print("Test passed !")


@pytest.mark.parametrize(
    "string, expected",
    [
        ("abcd", "a"),
        ("aabcc", "b"),
        ("aabcccccdd", "b"),
        ("aabbccc", "$"),
        ("banana", "b"),
        ("google", "l"),
        ("aabbc", "c"),
        ("abcabd", "c"),
        ("", "$"),
        ("aabcdd", "b"),
        ("abcabda", "c"),
    ],
)
def test_first_non_repeating_character(string, expected):
    print("Testing first non repeating character")
    assert first_non_repeating_character_approach1(string) == expected
    assert first_non_repeating_character_approach2(string) == expected
    print("Test passed !")


@pytest.mark.parametrize(
    "string, expected",
    [("V", 5), ("X", 10), ("IX", 9), ("MCMIV", 1904), ("XL", 40)],
)
def test_roman_to_integer(string, expected):
    print("Testing roman to integer")
    assert roman_to_integer(string) == expected
    print("Test passed !")


@pytest.mark.parametrize(
    "string, expected",
    [
        ("-123", -123),
        ("  -", 0),
        (" 1231231231311133", 2147483647),
        ("  -0012gfg4", -12),
        ("  00 12gc", 0),
    ],
)
def test_atoi(string, expected):
    print("Testing roman to integer")
    assert atoi_approch_1(string) == expected
    assert atoi_approch_2(string) == expected
    print("Test passed !")


@pytest.mark.parametrize(
    "input_string, encrypted_output",
    [
        ("aaaaaaaaaaa", "ba"),
        ("abc", "1c1b1a"),
        ("aaa", "3a"),
        ("aaabb", "2b3a"),
        ("abcd", "1d1c1b1a"),
        ("aaadddegggg", "4g1e3d3a"),
        ("zzzzzz", "6z"),
        ("aabbcc", "2c2b2a"),
        ("hellooo", "3o2l1e1h"),
        ("ppppqqr", "1r2q4p"),
        ("xyz", "1z1y1x"),
    ],
)
def test_encrypt_the_string(input_string, encrypted_output):
    print("Testing encrypt the string")
    assert encrypt_the_string(input_string) == encrypted_output
    print("Test passed !")


@pytest.mark.parametrize(
    "bracket_pattern, breaking_index",
    [
        ("(())))(", 4),
        ("))", -1),
        ("))()(()", 4),
        ("((()))", 3),
        ("()()", 2),
    ],
)
def test_equal_point_in_brackets(bracket_pattern, breaking_index):
    print("Testing equal point in brackets")
    assert equal_point_in_brackets_approach1(bracket_pattern) == breaking_index
    assert equal_point_in_brackets_approach2(bracket_pattern) == breaking_index
    print("Test passed !")


@pytest.mark.parametrize(
    "string1, string2, expected",
    [
        ("geeks", "kseeg", True),
        ("allergy", "allergyy", False),
        ("listen", "lists", False)
    ],
)
def test_check_anagram(string1, string2, expected):
    print("Testing equal point in brackets")
    assert check_anagram_approach1(string1, string2) == expected
    print("Test passed !")