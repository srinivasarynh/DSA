class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
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

    def insert_at_index(self, index, data):
        if index == 0:
            self.insert_front(data)
            return

        new_node = Node(data)
        curr_node = self.head

        for _ in range(index-1):
            if not curr_node:
                raise IndexError("index out of bounds")
            curr_node = curr_node.next

        new_node.next = curr_node.next
        curr_node.next = new_node

    def delete_front(self):
        if not self.head:
            raise IndexError("list is empty")
        self.head = self.head.next

    def delete_back(self):
        if not self.head:
            raise IndexError("list is empty")
        if not self.head.next:
            self.head = None
            return

        curr_node = self.head
        while curr_node.next.next:
            curr_node = curr_node.next
        curr_node.next = None

    def delete_at_index(self, index):
        if index == 0:
            self.delete_front()
            return
        curr_node = self.head
        for _ in range(index-1):
            if not curr_node:
                raise IndexError("index out of bounds")
            curr_node = curr_node.next

        if not curr_node.next:
            raise IndexError("index out of bounds")

        curr_node.next = curr_node.next.next

    def search(self, value):
        curr_node = self.head
        idx = 0
        while curr_node:
            if curr_node.data == value:
                return idx
            curr_node = curr_node.next
            idx += 1
        return -1

    def length(self):
        count = 0
        curr_node = self.head
        while curr_node:
            count += 1
            curr_node = curr_node.next

        return count

    def print_list(self):
        curr_node = self.head
        out = []
        while curr_node:
            out.append(str(curr_node.data))
            curr_node = curr_node.next
        print(" -> ".join(out) if out else "empty list")


ll = SinglyLinkedList()
ll.insert_front(1)
ll.insert_back(3)
ll.insert_at_index(1, 2)
ll.print_list()
