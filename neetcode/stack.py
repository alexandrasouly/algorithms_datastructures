# Description: Stack implementation
# Stacks have two main operations push and pop,
# push adds an element to the top of the stack,
# pop removes the top element of the stack,
# their complexity is O(1) for both operations


class Stack:
    def __init__(self) -> None:
        self.stack = []

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            return None

    def peek(self):
        if self.stack:
            return self.stack[-1]
        else:
            return None

    def is_empty(self):
        return self.stack == []


if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack.peek())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.is_empty())
