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
                print(n.data, end=" ==>")
                n = n.next

    def add_at_begining(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def add_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            print("Slinked List is Empty!")
        else:
            n = self.head
            while n.next is not None:
                n = n.next
            n.next = new_node

    def add_after_node(self, data, x):
        if self.head is None:
            print("Slinked List is Empty!")
            return

        n = self.head
        while n is not None:
            if x == n.data:
                break
            n = n.next
        
        if n is None:
            print("The Node Not Found!")
        else:
            new_node = Node(data)
            new_node.next = n.next
            n.next = new_node

    def add_before_node(self, data, x):
        if self.head is None:
            print("Slinked List is Empty!")
            return

        n = self.head
        while n is not None:
            if n.next.data == x:
                break
            n = n.next
        
        if n is None:
            print("The Node Not Found!")
        else:
            new_node = Node(data)
            new_node.next = n.next
            n.next = new_node

    def insert_when_empty(self, data):
        if self.head is None:
            new_node  = Node(data)
            self.head = new_node
        else:
            print("Couldn't Push Single Liked List Has Nodes")


    # Deleting Singly Linked List

    def delete_from_begin(self):
        if self.head is None:
            print("There is no Existing Head to be Removed")
        else:
            self.head = self.head.next

    def delete_at_last(self):
        if self.head is None:
            print("There Is No Last Node in The given Singly linked list")
        elif self.head.next is None:  # if the linked list contains only one node
            self.head = None
        else:
            n = self.head
            while n.next.next is not None:
                n = n.next
            n.next = None

    def delete_node_by_value(self, x):
        if self.head is None:
            print("LL is empty")
            return
        if x == self.head.data:
            self.head = self.head.next
            return
        n = self.head
        while n.next is None:
            if x == n.next.data:
                break
            n = n.next
        if n.next is None:
            print("Node is Not present")
        else:
            n.next = n.next.next


LL1 = SinglyLinkedList()
# LL1.printLinkedList()
LL1.add_at_begining(10)

LL1.add_at_end(5)

LL1.add_at_begining(20)

LL1.add_at_end(2)

LL1.add_after_node(10, 5)

LL1.add_before_node(7, 5)

LL1.insert_when_empty(100)

LL1.printLinkedList()

LL1.delete_from_begin()

LL1.delete_at_last()

LL1.delete_node_by_value(5)
print()
LL1.printLinkedList()
