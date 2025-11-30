"""
Algorithm: KMP (Knuth-Morris-Pratt Pattern Matching)
Purpose: KMP is used to search for a pattern within a string efficiently by preprocessing the pattern to create an LPS (Longest Prefix which is also Suffix) table.
"""


def build_lps_array(pattern):
    """
    Build the Longest Prefix Suffix (LPS) array.
    LPS helps us skip unnecessary comparisons by storing
    the length of the longest prefix that is also a suffix.
    """
    lps_array = [0] * len(pattern)
    prefix_length = 0
    current_index = 1

    while current_index < len(pattern):
        if pattern[current_index] == pattern[prefix_length]:
            prefix_length += 1
            lps_array[current_index] = prefix_length
            current_index += 1
        else:
            if prefix_length != 0:
                prefix_length = lps_array[prefix_length - 1]
            else:
                lps_array[current_index] = 0
                current_index += 1
    return lps_array


def kmp_search(text, pattern):
    """
    Perform KMP search to check if 'pattern' exists in 'text'.
    Returns True if found, False otherwise.
    """
    lps_array = build_lps_array(pattern)
    text_index = 0
    pattern_index = 0

    while text_index < len(text):
        if text[text_index] == pattern[pattern_index]:
            text_index += 1
            pattern_index += 1

            if pattern_index == len(pattern):
                return True
        else:
            if pattern_index != 0:
                pattern_index = lps_array[pattern_index - 1]
            else:
                text_index += 1
    return False


