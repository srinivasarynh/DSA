class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        self.head = new_node

    def insert_back(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        curr_node = self.head
        while curr_node.next:
            curr_node = curr_node.next

        curr_node.next = new_node
        new_node.prev = curr_node

    def insert_at_index(self, index, data):
        if index == 0:
            self.insert_front(data)
            return

        new_node = Node(data)
        curr_node = self.head
        for _ in range(index-1):
            if not curr_node:
                raise IndexError("Index out of bounds")
            curr_node = curr_node.next

        new_node.next = curr_node.next
        new_node.prev = curr_node

        if curr_node.next:
            curr_node.next.prev = new_node
        curr_node.next = new_node

    def delete_front(self):
        if not self.head:
            raise IndexError("list is empty")
        self.head = self.head.next
        if self.head:
            self.head.prev = None

    def delete_back(self):
        if not self.head:
            raise IndexError("list is empty")

        curr_node = self.head
        if not curr_node.next:
            self.head = None
            return

        while curr_node.next:
            curr_node = curr_node.next

        curr_node.prev.next = None

    def delete_at_index(self, index):
        if index == 0:
            self.delete_front()
            return

        curr_node = self.head
        for _ in range(index):
            if not curr_node:
                raise IndexError("index out of bounds")
            curr_node = curr_node.next

        if curr_node.prev:
            curr_node.prev.next = curr_node.next
        if curr_node.next:
            curr_node.next.prev = curr_node.prev

    def print_forward(self):
        curr_node = self.head
        out = []
        while curr_node:
            out.append(str(curr_node.data))
            curr_node = curr_node.next
        print(" <-> ".join(out) if out else "empty list")

    def print_backward(self):
        curr_node = self.head
        while curr_node and curr_node.next:
            curr_node = curr_node.next
        out = []
        while curr_node:
            out.append(str(curr_node.data))
            curr_node = curr_node.prev
        print(" <-> ".join(out) if out else "empty list")


dll = DoublyLinkedList()
dll.insert_front(1)
dll.insert_back(3)
dll.insert_at_index(2, 2)
dll.print_forward()
