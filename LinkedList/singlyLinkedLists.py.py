class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:

    def __init__(self):
        self.head = None

    def printLinkedList(self):
        if self.head is None:
            print("Linked List Is Empty")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.next

    def add_at_begining(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

LL1 = SinglyLinkedList()
LL1.printLinkedList()
LL1.add_at_begining(10)
LL1.add_at_begining(20)
LL1.printLinkedList()
