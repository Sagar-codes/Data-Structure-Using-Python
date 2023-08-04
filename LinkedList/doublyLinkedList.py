class Node:
    def __init__(self, data):
        self.data = data
        self.pref = None
        self.nref = None


class DoublyLinkedList:
    
    def __init__(self) -> None:
        self.head = None

    def traversal(self):
        if self.head is None:
            print("Forward: Doubly Linked List Is Empty")
        else:
            n = self.head
            while n is not None:
                print(n.data, end=" ==>")
                n = n.nref
                
    def backwardTraversal(self):
        if self.head is None:
            print("Backward: Doubly Linked List Is Empty")
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref

            while n is not None:
                print(n.data, end=" <==")
                n = n.pref
        
    def insert_when_empty(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("DLL is not empty")
    
    def insert_at_begin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.nref = self.head
            self.head.pref = new_node
            self.head = new_node
        
    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n is None:
                n = n.nref
            n.nref = new_node
            new_node.pref = n

    def add_after_given(self, data, x):
        if self.head is None:
            print("You cannot insert cz the DLL is Empty")

        else:
            n = self.head
            while n is not None:
                if x == n.data:
                    break
                n = n.nref
            if n is None:
                print("Given Node Is not present in the DLL ")
            else:
                new_node = Node(data)
                new_node.nref = n.nref
                new_node.pref = n
                if n.nref is not None:
                    n.nref.pref = new_node
                n.nref = new_node


    def add_before_given(self, data, x):
        if self.head is None:
            print("DLL is Empty")
        
        else:
            n = self.head
            while n is not None:
                if x == n.data:
                    break
                n = n.nref
            if n is None:
                print("Given Node Is not present in DLL")

            else:
                new_node = Node(data)
                new_node.nref = n
                new_node.pref = n.pref
                if n.pref is not None:
                    n.pref.nref = new_node
                else:
                    self.head = new_node
                n.pref = new_node

    # delete Operation

    def delete_begin(self):
        if self.head is None:
            print("DLL is Empty")
            return

        if self.head.nref is None:
            self.head = None
            print("DLL is empty after deleting first node")
        else:
            self.head = self.head.nref
            self.head.pref = None

    def delete_end(self):
        if self.head is None:
            print("DLL is empty")
            return

        if self.head.nref is None:
            self.head = None
            print("DLL is empty after deleting first Node")

        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            n.pref.nref = None

    def delete_by_value(self, x):
        if self.head is None:
            print("DLL is Empty")
            return

        n = self.head
        if n.nref is None:
            if x == n.data:
                self.head = None
            else:
                print("The Given Value is not present in the data")
            return
        
        if self.head.data == x:
            self.head = self.head.nref
            self.head.pref = None
            return
        
        n = self.head
        while n.nref is not None:
            if x == n.data:
                break
            n = n.nref
        if n.nref is not None:
            n.nref.pref = n.pref
            n.pref.nref = n.nref
        else:
            if n.data == x:
                n.pref.nref = None
            else:
                print("The Given value is Not present in the DLL X")



DLL = DoublyLinkedList()

DLL.insert_at_begin(10)

DLL.insert_at_end(20)

DLL.add_after_given(15, 10)

DLL.add_before_given(5, 10)

DLL.delete_begin()

DLL.delete_end()

DLL.delete_by_value(15)

DLL.traversal()
# DLL.backwardTraversal()