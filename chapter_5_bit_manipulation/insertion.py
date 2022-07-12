# insert m into n between jth and ith bits

# we first clear the middle bits with the mask, and then add the m shifted to the middle

def insertion(n: int, m: int, i: int, j: int):
    mask = (-1 << (j+1)) | ((1 << i) - 1)
    return (n & mask) | m << i


if __name__ == '__main__':
    assert insertion(int("10000000000", 2), int(
        "10011", 2), 2, 6) == int("10001001100", 2)
    assert insertion(int("11111111111", 2), int(
        "10011", 2), 2, 6) == int("11111001111", 2)
