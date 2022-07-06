# delete node from singly linked list given access only to that node


from linked_list import LinkedList, Node


def delete_node_singly(node: Node):
    node.data = node.next.data
    node.next = node.next.next

# WHY Does this not work?
def delete_node_singly(node: Node):
    node = node.next


if __name__ == "__main__":
    linked_list = LinkedList([1, 5, 1, 3, 4, 3, 4, 2, 3, 5, 1, 10])

    node_to_delete = linked_list.head.next.next.next
    print(f"we will be deleting {node_to_delete}")
    delete_node_singly(node_to_delete)
    print(linked_list)
