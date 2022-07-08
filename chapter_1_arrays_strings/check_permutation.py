from collections import Counter

# Check if one string is a permutation of the other one

# O(nlogn)


def check_permutation_with_sort(str1: str, str2: str):
    if len(str1) != len(str2):
        return False
    str1 = sorted(str1)
    str2 = sorted(str2)

    for char1, char2 in zip(str1, str2):
        if char1 != char2:
            return False
    return True


# O(n), but additional space
def check_with_dict(str1: str, str2: str):
    counts = Counter(str1)
    for char in str2:
        if not char in counts:
            return False
        else:
            counts[char] -= 1
    if any(counts.values()):
        return False
    return True


if __name__ == '__main__':
    print(check_permutation_with_sort('abccc', 'accbc'))
    print(check_permutation_with_sort('abcccd', 'accbc'))
    print(check_with_dict('abccc', 'accbc'))
    print(check_with_dict('abcccd', 'accbc'))
