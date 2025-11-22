class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_front(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = new_node
            return

        curr_node = self.head
        while curr_node.next != self.head:
            curr_node = curr_node.next

        curr_node.next = new_node
        new_node.next = self.head
        self.head = new_node

    def insert_back(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = new_node
            return

        curr_node = self.head
        while curr_node.next != self.head:
            curr_node = curr_node.next

        curr_node.next = new_node
        new_node.next = self.head

    def delete_back(self):
        if not self.head:
            raise IndexError("list is empty")

        curr_node = self.head
        while curr_node.next != self.head:
            prev = curr_node
            curr_node = curr_node.next

        if prev is None:
            self.head = None
        else:
            prev.next = self.head

    def print_list(self):
        if not self.head:
            print("empty list")
            return

        curr_node = self.head
        out = []
        while True:
            out.append(str(curr_node.data))
            curr_node = curr_node.next
            if curr_node == self.head:
                break

        print(" -> ".join(out) + "-> (back to head)")


cll = CircularLinkedList()
cll.insert_front(1)
cll.insert_back(2)
cll.insert_back(3)
cll.print_list()
