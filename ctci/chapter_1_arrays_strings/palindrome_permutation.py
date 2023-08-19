# whether a plaindorme permutaiton exists
from collections import Counter
import string


def has_palindrome_permutation(my_str: str):
    my_str = clean(my_str)
    counts = Counter(my_str)
    # odd length, we need one singular, every other even
    # even lenght, we need all of them even
    return sum(val % 2 for val in counts.values()) <= 1


def clean(my_str: str):
    return ''.join([c for c in my_str.lower() if c in string.ascii_lowercase])
