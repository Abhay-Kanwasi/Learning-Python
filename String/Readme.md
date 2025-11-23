# String

Python string is a collection of Unicode characters.

Python can be enclosed in single, double, triple quotes.

a = 'asdfsd' # 'that\'s' |
a = "sdfsdf"
a = """asdfsdf""" # docstring, information

string = abhay
01234 (Positive indexing)
-5-4-3-2-1 (Negative indexing)
# string[3], string[-2], string[0:4]

- string elements can be accessed using an index value, it starts with 0. Negative indexing is allowed. THe last character is considered to be at index -1.
- A substring can be sliced out of a string:
  - string[start:end] - extract from start to end - 1 
  - string[start:] - extract from start to end.
  - sting[:end] - extract from start to end -1.
  - string[-start:] - extract from -start(included) to end.
  - string[:-end] - extract from the beginning to -end -1.

String properties
- All strings are objects of built-in type str.
- Is string mutable or not ? : No not mutable and they cannot be changed.
- Strings can be concatenated using '+'.
- chr returns a string representing its Unicode value(known as code point). ord does reverse
