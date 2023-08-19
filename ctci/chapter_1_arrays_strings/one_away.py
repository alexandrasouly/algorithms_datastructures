# edits permitted: insert, remove or replace a character
# check if two strings are one away


def one_away(str1, str2):
    print(str1 + ' ' + str2)
    # if same word, done
    if str1 == str2:
        return True
    # if length matches, we need one letter diff
    elif len(str1) == len(str2):
        return replace_needed(str1, str2)
    # if length one away, we need a deletion/insertion
    elif abs(len(str1) - len(str2)) == 1:
        return insert_needed(str1, str2)
    # otherwise can't be one away
    else:
        return False


def replace_needed(str1, str2):
    off = 0
    for char1, char2 in zip(str1, str2):
        if char1 != char2:
            off += 1
    if off > 1:
        return False
    else:
        return True


def insert_needed(str1, str2):
    short = str1 if len(str1) < len(str2) else str2
    long = str1 if len(str1) > len(str2) else str2
    off = 0
    i = 0
    j = 0
    while i < len(short) and j < len(long):
        if short[i] != long[j]:
            off += 1
            j += 1
        i += 1
        j += 1
    if off > 1:
        return False
    return True


if __name__ == '__main__':
    print(one_away('pale', 'pale'))
    print(one_away('pale', 'longword'))
    print(one_away('pale', 'ple'))
    print(one_away('pale', 'pales'))
    print(one_away('ale', 'pale'))
    print(one_away('pale', 'bale'))
    print(one_away('pale', 'bake'))
