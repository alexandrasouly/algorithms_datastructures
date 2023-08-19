# Queue using linked lists
# we want O(1) for enqueue and dequeue


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, val):
        node = Node(val)
        if self.head is None:
            self.head = node
            self.tail = node
            return
        self.tail.next = node
        self.tail = node

    def dequeue(self):
        if self.head is None:
            return None
        val = self.head.val
        self.head = self.head.next
        return val

    def peek(self):
        if self.head is None:
            return None
        return self.head.val
