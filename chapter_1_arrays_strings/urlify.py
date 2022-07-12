# replace whitespace with %20 in a string


# not optimal, .replace() is definitely not O(n) as it needs to recopy the list
# every time
def pythonic(my_str: str, length: int):
    return my_str[:length].replace(" ", "%20")


# we can't modify chars in place
# so i'm just gonna convert them to list for the q to make sense
# O(n) solution
def algorithmic(my_str: str, length: int):
    my_str = list(my_str)
    last_letter_idx = length-1
    write_to_idx = len(my_str)-1
    while last_letter_idx >= 0:
        if my_str[last_letter_idx] != ' ':
            my_str[write_to_idx] = my_str[last_letter_idx]
            write_to_idx -= 1
            last_letter_idx -= 1
        else:
            my_str[write_to_idx-2:write_to_idx+1] = '%20'
            write_to_idx -= 3
            last_letter_idx -= 1
    return ''.join(my_str)


if __name__ == '__main__':
    print(algorithmic('Mr John Smith    ', length=13))
