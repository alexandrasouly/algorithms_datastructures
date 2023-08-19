# check w one call to is_substring whether s1 is a rotation to s2


def check_rotation(s1, s2):
    if len(s1) != len(s2) or len(s1) == 0:
        return False
    return is_substring(s1, s2+s2)


def is_substring(s1: str, s2: str):
    return s1 in s2


if __name__ == '__main__':
    print(check_rotation('waterbottle', 'erbottlewat'))
