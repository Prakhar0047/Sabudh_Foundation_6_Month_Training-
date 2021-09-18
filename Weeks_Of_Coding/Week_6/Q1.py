class Node():
    """
    A function to create new node so that we don't have to rewrite code to instantiate a new node in every function.
    """

    def __init__(self,data): # This will help us to store data in node we will initiate
        self.data = data # This is link to the data
        self.next = None # This will act as next. At first it will be null because there is no other node


class LinkedList():
    """
    Linked list class with full functionality like: append, prepend, printList, insert, delete
    """
    # Here we are initiating list. As at starting list will be empty So head will point to null and tail will point to head.
    def __init__(self):
        self.head = None
        self.tail = self.head
        self.length = 0


    def append(self,data):
        """
        A function to add node at the last.
        """
        new_node = Node(data)
        
        if self.head == None:
            self.head = new_node
            self.tail = self.head
            self.length = 1
        else:
            self.tail.next = new_node # In this node we are shifting pointer to the new node as a new node is appended in to the list
            self.tail = new_node # Here we are pointing tail to the new node (Already present node will point to new node.)
            self.length+=1 # Increase the length of the list.


    def prepend(self,data):
        """
        A function to add node at index = 0 in linked list.
        """
        new_node = Node(data)
        new_node.next = self.head # Jo new node ka next attri hai vo abb puranai head ko point karega
        self.head = new_node # New Node new head hai
        self.length+=1


    def print_list(self):
        """
        A function to print list.
        """
        if self.head == None:
            print("Empty List.")
        else:
            current_node = self.head
            while current_node != None:
                print(current_node.data, end='')
                current_node = current_node.next
        print()


    def insert(self,index,data):
        """
        A function to insert an node in desired location.
        """
        if index >= self.length:
            if index > self.length:
                print("Position not available Appending at last.")
            new_node = Node(data)
            self.tail.next = new_node
            self.tail = new_node
            self.length+=1

        elif index == 0:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            self.length+=1

        else:
            new_node = Node(data)
            current_node = self.head
            for i in range(index-1):
                current_node = current_node.next
            new_node = current_node.next
            current_node.next = new_node
            self.length+=1

    def reverse(self):
        """
        A function for revesing Linked List
        """
        prev = None
        current = self.head
        # Will go till we meet end..
        while(current is not None):
            next = current.next 
            current.next = prev # Reverse
            prev = current 
            current = next
        self.head = prev # After all end move eHead to end so it gets reversed.

llist = LinkedList()
llist.append(1)
llist.append(2)
llist.append(3)
llist.append(4)
print("Linked List")
llist.print_list()
llist.reverse()
print("Linked List After Reversed")
llist.print_list()