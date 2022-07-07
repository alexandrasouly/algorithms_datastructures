from pickle import TRUE
from turtle import Turtle, back
from linked_list import LinkedList

def palindrome(linked_list: LinkedList):
    is_palindrome = True
    stack = get_stack(linked_list)
    forward_node = linked_list.head
    backward_node = stack.head
    while forward_node:
        if forward_node.data != backward_node.data:
            is_palindrome = False
        forward_node = forward_node.next
        backward_node = backward_node.next

    return is_palindrome

def get_stack(linked_list):
    # I could just append to a list here, but I have
    # a functioning linked list class anyway 
    stack = LinkedList()
    for node in linked_list:
        stack.add_node_to_head(node.data)
    return stack

if __name__ == '__main__':
    linked_list = LinkedList([1, 5, 3, 5, 1])
    print(palindrome(linked_list))
    linked_list = LinkedList([1, 5, 2, 1])
    print(palindrome(linked_list))