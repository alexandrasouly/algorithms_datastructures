# kth to last meaning 0th to last is last, 1st to last is one before the last etc...

# common tool is to use multiple pointers in a linked list
# here we have two pointers with k distance, and when the last one hits the end
# the first one will be at the kth to last element

from linked_list import LinkedList


def kth_to_last(k: int, linked_list: LinkedList):
    ''' Returns kth to last element of a linked list'''

    lp = linked_list.head
    for i in range(k):
        if lp:
            lp = lp.next
        else:
            raise RuntimeError(
                f'linked list is length {i+1}, but {k}th to last was asked.')
    fp = linked_list.head

    while lp and lp.next:
        lp = lp.next
        fp = fp.next

    return fp.data


if __name__ == "__main__":

    linked_list = LinkedList([1, 5, 1, 3, 4, 3, 4, 2, 3, 5, 1, 10])
    print(kth_to_last(2, linked_list))
