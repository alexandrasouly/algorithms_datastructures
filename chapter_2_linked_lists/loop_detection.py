# find out if a linked list has a loop

from linked_list import LinkedList
def is_loop(ll):
    ptr1 = ll.head
    ptr2 = ll.head
    while ptr1 and ptr2.next:
        ptr1 = ptr1.next
        ptr2 = ptr2.next.next
        if ptr1 is ptr2:
            return ptr1
    return None


def find_cycle(cycle_ptr):
    current = cycle_ptr.next
    counter = 1
    while cycle_ptr is not current:
        current = current.next
        counter += 1

    return counter 


def main(ll:LinkedList):
    # is there a cycle?
    # one pointer twice as fast as the other
    cycle_ptr = is_loop(ll)
    if cycle_ptr:
        # we find the cycle length by going around the cycle
        cycle = find_cycle(cycle_ptr)
        # we put a ppointer at the beginning
        # one at cycle length distance from it
        ptr1 = ll.head
        ptr2 = ll.head
        for _ in range(cycle):
            ptr2 = ptr2.next
        # they will meet exacxtly at the beginning of the cycle
        while ptr1 is not ptr2:
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        return ptr1
    return None


if __name__ == '__main__':
    linked_list_loop = LinkedList([100, 5, 3, 5, 1])
    linked_list1 = LinkedList([4,5,6,8,9])
    print(main(linked_list1))
    linked_list_loop.tail.next = linked_list_loop.head
    linked_list1.tail.next = linked_list_loop.head
    print(main(linked_list1))