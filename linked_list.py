

from typing import Optional


class Node:

    def __init__(self, data, prev=None, next=None):
        self.next: Optional[Node] = next
        self.prev: Optional[Node] = prev
        self.data = data

    def __str__(self):
        return str(self.data)


class LinkedList:
    '''
    Doubly linked list implementation

    For a singly linked list, just don't set prev on Nodes. 
    In this case you need to iterate through the list to delete from tail.
    Keeping a pointer to the tail wouldn't be necessary either.

    '''

    def __init__(self, values=None) -> None:
        self.head = None  # where it starts, to go forwards
        self.tail = None  # where it ends, to go backwards

        if values:
            self.create_with_values(values)

    def __str__(self):
        values = [str(x) for x in self]
        return ' -> '.join(values)

    def __iter__(self) -> None:
        current = self.head
        while current:
            yield current
            current = current.next

    def create_with_values(self, values):
        ''' Initialise a linked list from an iterator '''
        for value in values:
            self.add_node_to_tail(value)

    def add_node_to_tail(self, value):
        ''' Add a node at the tail of the list'''
        if not self.tail:
            self.tail = self.head = Node(value)
        else:
            # if not doubly linked just omit the prev bits
            self.tail.next = Node(value, prev=self.tail)
            self.tail = self.tail.next

    def add_node_to_head(self, value):
        ''' Add a node at the head of the list'''
        if not self.head:
            self.tail = self.head = Node(value)
        else:
            self.head.prev = Node(value, next=self.head)
            self.head = self.head.prev

    def delete_from_head(self):
        if not self.head:
            return
        self.head = self.head.next
        if self.head:
            self.head.prev = None

    def delete_from_tail(self):
        if not self.tail:
            return
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None

    def delete_node_doubly(self, node: Node):
        if node.next:
            node.next.prev = node.prev
        if node.prev:
            node.prev.next = node.next


if __name__ == '__main__':
    linkedlist = LinkedList([1, 2, 3, 4, 5])
    for element in linkedlist:
        print(element)

    linkedlist.add_node_to_head(0)
    linkedlist.add_node_to_tail(6)
    print(linkedlist)
    linkedlist.delete_from_head()
    linkedlist.delete_from_tail()
    print(linkedlist)
