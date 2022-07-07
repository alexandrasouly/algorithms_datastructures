# Two linked lists are the digits of two numbers stored in reverse order
# Add them together without converting to ints

from linked_list import LinkedList, Node


def sum_lists_reverse(list1: LinkedList, list2: LinkedList):
    sum_list = LinkedList()
    left = list1.head
    right = list2.head
    carry_over = 0
    while left or right:
        left_num = left.data if left else 0
        right_num = right.data if right else 0
        sum = left_num + right_num + carry_over
        if sum >9:
            next_carry_over = 1
            sum = sum -10
        else:
            next_carry_over = 0
        sum_list.add_node_to_tail(sum)
        if left:
            left = left.next
        if right:        
            right = right.next
        carry_over = next_carry_over
    if carry_over:
        sum_list.add_node_to_tail(carry_over)

    return sum_list

# now assume they are stored in order 
def sum_lists(list1:LinkedList, list2:LinkedList):
    # we start to add some padding to get equal digits
    len1 = len(list1)
    len2 = len(list2)
    if len1 > len2:
        pad_list(list2, len1-len2)
    elif len1 < len2:
        pad_list(list1, len2-len1)

    another_round_needed = False
    current_left = list1.head
    current_right = list2.head
    sum_list = LinkedList()
    # here we just add them together, might end up with numebrs bigger than two
    for _ in range(max(len1,len2)):
        digit = current_left.data + current_right.data
        sum_list.add_node_to_tail(digit)
        if digit >9:
            another_round_needed = True
        current_left = current_left.next
        current_right = current_right.next
    # iterate through the list as many times as needed, 
    # sorting out the carry overs one by one from the front
    # until we don't have digits bigger than 10

    while another_round_needed:
        another_round_needed = False
        for node in sum_list:
            if node.next and node.next.data>9:
                node.data +=1
                node.next.data -= 10
                if node.data > 9:
                    another_round_needed = True
    # sorting out the first
    if sum_list.head.data >9:
        sum_list.add_node_to_head(1)
        sum_list.head.next.data  -= 10
    return sum_list


def pad_list(linked_list: LinkedList, zeros: int):
    for _ in range(zeros):
        linked_list.add_node_to_head(0)

if __name__ == "__main__":
    linked_list1 = LinkedList([1, 7,3,9])
    linked_list2 = LinkedList([5,9,6])
    print(f"we will be adding 9371 + 695 = 10066")
    print(sum_lists_reverse(linked_list1, linked_list2))
    # now the forward ones
    linked_list1 = LinkedList([9,9,9,9])
    linked_list2 = LinkedList([1,1,1,1])
    print(f"we will be adding 9999 + 1111 = 11110")
    print(sum_lists(linked_list2, linked_list1))
    linked_list1 = LinkedList([9,9,9,9])
    linked_list2 = LinkedList([2])
    print(f"we will be adding 9999 + 2 = 10001")
    print(sum_lists(linked_list2, linked_list1))