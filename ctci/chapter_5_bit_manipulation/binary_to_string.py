# real number between 0 and 1
# print binary representation
# if can't be repr with 32 chars or less, error


# if the numbers are small there could be division errors so I start by multiplying by 2**32
def binary_to_string(num: int):
    if not 1 > num > 0:
        return 'input should be between 0 and 1 '
    big_num = num * (2**32)
    if big_num - int(big_num) != 0:
        return 'error, cannot be repred with 32 bits'
    big_num = int(big_num)
    repr = '0.'
    n = 31
    while big_num > 0:
        if big_num >= 2**n:
            repr += '1'
            big_num -= 2**n
        else:
            repr += '0'
        n -= 1

    return repr


if __name__ == '__main__':
    assert(binary_to_string(0.5000000004656612873077392578125)
           ) == '0.1000000000000000000000000000001'  # 2^(-31) + 1/2
    assert(binary_to_string(0.3)) == 'error, cannot be repred with 32 bits'
