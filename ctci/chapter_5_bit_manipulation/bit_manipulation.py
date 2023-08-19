# basic bit manipulation functions

def get_bit(i: int, num: int):
    '''Get ith bit of a num'''
    return (num & (1 << i)) != 0


def set_bit(i: int, num: int):
    ''' Set ith bit of num to 1'''
    return num | (1 << i)


def clear_bit(i: int, num: int):
    ''' Clear ith bit of num to 0'''
    mask = ~ (1 << i)
    return num & mask


def clear_first_i_bits(i: int, num: int):
    '''clear the first i bits of num starting from the most significant one'''

    mask = (1 << i) - 1
    return num & mask


def clear_last_i_bits(i: int, num: int):
    '''clear the last i bits of num starting from the least significant one'''

    mask = -1 << (i+1)
    return num & mask


def update_bit(i: int, num: int, is1: bool):
    value = 1 if is1 else 0
    clear_mask = ~(1 << i)

    return (num & clear_mask) | (value << i)
