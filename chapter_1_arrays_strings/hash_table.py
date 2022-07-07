INITIAL_CAPACITY = 10
# Python implementation of a hash table, using an array of linked lists
# and the built-in hash function.

# implementation heavily based on
# https://stephenagrice.medium.com/how-to-implement-a-hash-table-in-python-1eb6c55019fd
# with some fixes/improvements


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.key + ":" + self.value + str(self.next))


class HashTable:
    def __init__(self):
        self.capacity = INITIAL_CAPACITY  # how long is our array
        self.size = 0  # how many items we currently have
        self.buckets = [None] * self.capacity  # our array

    def __str__(self):
        return str([str(element) for element in self.buckets])

    def hash(self, key):
        hashsum = hash(key)
        hashsum = hashsum % self.capacity
        return hashsum

    def insert(self, key, value):
        # 1. Increment size
        self.size += 1
        # 2. Compute index of key
        index = self.hash(key)
        # Go to the node corresponding to the hash
        node = self.buckets[index]
        # 3. If bucket is empty:
        if not node:
            # Create node, add it, return
            self.buckets[index] = Node(key, value)
            return
        # 4. Collision! Check if we need to update a value or insert a new one at the end
        prev = None
        while node:
            next_node = node.next
            # Update value
            if node.key == key:
                new_node = Node(key, value)
                if prev:
                    prev.next = new_node
                    new_node.next = next_node
                else:
                    self.buckets[index] = new_node
                return
            prev = node
            node = node.next
        # Add a new node at the end of the list with provided key/value
        prev.next = Node(key, value)

    def find(self, key):
        # 1. Compute hash
        index = self.hash(key)
        # 2. Go to first node in list at bucket
        node = self.buckets[index]
        # 3. Traverse the linked list at this node
        while node is not None and node.key != key:
            node = node.next
        # 4. Now, node is the requested key/value pair or None
        if node is None:
            # Not found
            return None
        else:
            # Found - return the data value
            return node.value

    def remove(self, key):
        # 1. Compute hash
        index = self.hash(key)
        node = self.buckets[index]
        prev = None
        # 2. Iterate to the requested node
        while node and node.key != key:
            prev = node
            node = node.next
        # Now, node is either the requested node or none
        if node is None:
            # 3. Key not found
            return None
        else:
            # 4. The key was found.
            self.size -= 1
            result = node.value
            # Delete this element in linked list
            # first element in linked list
            if prev is None:
                # not the last element
                if node.next:
                    self.buckets[index] = node.next
                # only one element in linked list
                else:
                    self.buckets[index] = None
            # not first elements
            else:
                prev.next = prev.next.next
            # Return the deleted language

            return result


if __name__ == "__main__":
    table = HashTable()
    table.insert("1", "hi")
    table.insert("2", "hii")
    table.insert("3", "hello")
    table.insert("2", "new hii")

    print(table)
    print(table.find("1"))
    print(table.find('2'))
    print(table.find("3"))
    print('remove 2')
    table.remove("2")
    print(table)
    print('remove 1')
    table.remove("1")
    print(table)
    print('remove')
    table.remove("3")
    print(table)
