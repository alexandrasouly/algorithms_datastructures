# determine if a string is made of unique characters

# O(n) time, O(n) space solution: O(n) to add to add n letter to set, built-in len() is O(1)
def pythonic_hack(my_string: str):
    return len(set(my_string)) == len(my_string)


# technically O(1), will never go through more than number of characters in ASCII/Unicode
def use_a_set(my_str: str):
    my_set = set()
    for letter in my_str:
        if letter not in my_set:
            my_set.add(letter)
        else:
            return False
    return True


# create an array of all the characters and check if our one is in it
# could use a bitmap too here to reduce storage
def is_unique_chars_algorithmic(string):
    # Assuming character set is ASCII (128 characters)
    if len(string) > 128:
        return False

    # this is a pythonic and faster way to initialize an array with a fixed value.
    #  careful though it won't work for a doubly nested array
    char_set = [False] * 128
    for char in string:
        val = ord(char)
        if char_set[val]:
            # Char already found in string
            return False
        char_set[val] = True

    return True
