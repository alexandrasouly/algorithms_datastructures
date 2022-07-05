# Partition a linked list around a value
# st nodes less than x are in the left, x and bigger are in the right
# order within partition is not needed

from linked_list import LinkedList, Node


def partition(linked_list: LinkedList, x: int):
    first_half = None
    second_half = None

    node: Node
    for node in linked_list:
        if node.data < x:
            if first_half:
                first_half.next = node
            else:
                first_half = node
        elif node.data >= x:
            if second_half:
                second_half.next = node
            else:
                second_half = node

    print(linked_list)


def add_partition_after_node(node: Node):
    partition_node = Node("partition")
    partition_node.next = node.next
    node.next = partition_node


if __name__ == "__main__":
    linked_list = LinkedList([1, 5, 1, 3, 4, 11, 8, 3, 4, 2, 3, 5, 1, 10])
    x = 5
    print(f"we will be partitioning around {x}")

    partition(linked_list, x)
    print(linked_list)
