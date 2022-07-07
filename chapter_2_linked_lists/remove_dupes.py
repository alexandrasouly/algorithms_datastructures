from linked_list import LinkedList, Node

# singly linked list is enough
# __iter__ and delete specific node implementations needed

# O(n) time, O(n) space
def remove_dupes(linked_list: LinkedList):
    seen = set()
    element: Node
    for element in linked_list:
        if element.data in seen:
            linked_list.delete_node(element)
        else:
            seen.add(element.data)

    return linked_list

# O(n^2) time, no additional space
def remove_dupes_no_buffer(linked_list: LinkedList):
    element: Node
    for element in linked_list:
        # checking if this element exists later in the list
        # if yes, delete the later one
        current = element.next
        while current:
            next = current.next
            if current.data == element.data:
                linked_list.delete_node(current)
            current = next
    return linked_list


if __name__ == "__main__":

    linked_list = LinkedList([1, 5, 1, 3, 4, 3, 4, 2, 3, 5, 1, 10])
    print(remove_dupes(linked_list))
    linked_list = LinkedList([2, 1, 5, 1, 3, 4, 3, 4, 2, 3, 5, 1, 10, 1, 1, 1])
    print(remove_dupes_no_buffer(linked_list))
