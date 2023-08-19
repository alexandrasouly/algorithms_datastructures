# Description: Implementation of a linked list
# Linked lists are a linear data structure, elements are not stored in contiguous memory locations
# Each element is called a node
# Each node has two items, data and a reference to the next node


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class DoublyNode:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, node, data):
        new_node = Node(data)
        new_node.next = node.next
        node.next = new_node

    def remove_node(self, node):
        # this is O(n) as you need to traverse the list to find the node
        if node == self.head:
            self.head = node.next
            node = None
            return
        prev_node = self.head
        while prev_node.next != node:
            prev_node = prev_node.next
        prev_node.next = node.next
        node = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_beginning(self, data):
        new_node = DoublyNode(data)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        self.head = new_node

    def insert_after_node(self, node, data):
        new_node = DoublyNode(data)
        new_node.next = node.next
        new_node.prev = node
        if node.next:
            node.next.prev = new_node
        node.next = new_node

    def remove_node(self, node):
        # this is O(1) as doubly linked
        if node == self.head:
            self.head = node.next
            node = None
            return
        if node == self.tail:
            self.tail = node.prev
            node = None
            return
        node.prev.next = node.next
        node.next.prev = node.prev
        node = None


if __name__ == "__main__":
    linked_list = LinkedList()
    print(linked_list.head)
    linked_list.insert_at_beginning(1)
    linked_list.insert_at_beginning(2)
    linked_list.insert_at_beginning(3)
    print(linked_list.head.data)
    print(linked_list.head.next.data)
    print(linked_list.head.next.next.data)
    linked_list.insert_after_node(linked_list.head.next, 4)
    print(linked_list.head.next.next.data)
    linked_list.remove_node(linked_list.head.next)
