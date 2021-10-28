class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


# first = Node(3)
# print(first.data) #3
# print(first.next) #None

class SLL:
    def __init__(self):
        self.head = None

    def insert(self, data):
        newNode = Node(data)
        if self.head:
            curNode = self.head
            while curNode.next:
                curNode = curNode.next
            curNode.next = newNode
        else:
            self.head = newNode

    def printLL(self):
        curNode = self.head
        while curNode:
            print(curNode.data)
            curNode = curNode.next


first = SLL()
# first.head = Node(4)
# print(first.head.data)

first.insert(30)
first.insert(40)
first.insert(50)
first.printLL()


'''
# A single node of a singly linked list
class Node:
    # constructor
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


# A Linked List class with a single head node
class LinkedList:
    def __init__(self):
        self.head = None

    # insertion method for the linked list
    def insert(self, data):
        newNode = Node(data)
        if (self.head):
            current = self.head
            while (current.next):
                current = current.next
            current.next = newNode
        else:
            self.head = newNode

    # print method for the linked list
    def printLL(self):
        current = self.head
        while (current):
            print(current.data)
            current = current.next


# Singly Linked List with insertion and print methods
LL = LinkedList()
LL.insert(3)
LL.insert(4)
LL.insert(5)
LL.printLL()
'''