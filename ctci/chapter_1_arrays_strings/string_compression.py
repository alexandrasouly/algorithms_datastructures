# replace characters w/ the number of repeats eg aabcccccaaa => a2b1c5a3
def string_compression(my_str: str):
    if needs_compression(my_str):
        compressed = []
        counter = 1
        for idx in range(1, len(my_str)):
            if my_str[idx] != my_str[idx-1]:
                compressed.append(my_str[idx-1])
                compressed.append(str(counter))
                counter = 1
            else:
                counter += 1
        # last one
        compressed.append(my_str[idx])
        compressed.append(str(counter))

        return ''.join(compressed)
    return my_str


def needs_compression(my_str: str):
    compressed_length = 0
    counter = 1
    for idx in range(1, len(my_str)):
        if my_str[idx] != my_str[idx-1]:
            compressed_length += 1+len(str(counter))
            counter = 1
        else:
            counter += 1
    # last one
    compressed_length += 1+len(str(counter))
    return (compressed_length < len(my_str))


if __name__ == '__main__':
    print(string_compression('aabcccccaaa'))
    print(string_compression('abcddeeeffff'))
    print(string_compression('aaaaaaaaaabababab'))
