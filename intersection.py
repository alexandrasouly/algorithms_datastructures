# Determine if two signly linked lists intersect, if yes find the intersection node by reference


from linked_list import LinkedList

def find_intersection(ll1, ll2):
    len1 = len(ll1)
    len2 = len(ll2)

    pointer1 = ll1.head
    pointer2 = ll2.head
    for _ in range(max(0, len1-len2)):
        pointer1 = pointer1.next
    for _ in range(max(0, len2-len1)):
        pointer2 = pointer2.next
    while pointer1:
        if pointer1 is pointer2:
            return pointer1
        pointer1 = pointer1.next
        pointer2 = pointer2.next
    return None         


if __name__ == '__main__':
    linked_list_common = LinkedList([1, 5, 3, 5, 1])
    linked_list1 = LinkedList([4,5,6,8,9])
    linked_list2 = LinkedList([2,8, 3])
    print(find_intersection(linked_list1, linked_list2))
    linked_list1.tail.next = linked_list_common.head
    linked_list2.tail.next = linked_list_common.head

    print(find_intersection(linked_list1, linked_list2))