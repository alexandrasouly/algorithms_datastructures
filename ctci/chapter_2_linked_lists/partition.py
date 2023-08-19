# Partition a linked list around a value
# st nodes less than x are in the left, x and bigger are in the right
# order within partition is not needed

from linked_list import LinkedList, Node


def partition(linked_list: LinkedList, x: int):

    smaller_tail = None
    bigger_tail = None
    for node in linked_list:
        if node.data < x:
            if not smaller_tail:
                smaller_tail = node
            else:
                smaller_tail.next = node
                smaller_tail = node
        elif node.data >= x:
            if not bigger_tail:
                bigger_tail = bigger_head = node
            else:
                bigger_tail.next = node
                bigger_tail = node
         
    add_partition_after_node(smaller_tail)
    smaller_tail.next.next = bigger_head


def add_partition_after_node(node: Node):
    partition_node = Node("partition")
    partition_node.next = node.next
    node.next = partition_node


if __name__ == "__main__":
    linked_list = LinkedList([1, 5, 1, 3, 4, 11, 8, 3, 4, 2, 3, 5, 1, 10])
    x = 4
    print(f"we will be partitioning around {x}")

    partition(linked_list, x)
    print(linked_list)
