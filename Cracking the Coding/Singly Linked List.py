# Hello World program in Python
    
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class LinkedList:
    def __init__(self):
        self.head=None
        
    def traverselist(self):
        if self.head is None:
            print("The list is empty")
            return
        
        curr=self.head
        while curr is not None:
            print(curr.data, " ")
            curr = curr.next
    
    def insert_at_start(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        print("Node added to the start")
        return
    
    def insert_at_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        curr = self.head
        while curr.next is not None:
            curr = curr.next
            
        curr.next = new_node
        print("Node added to the end")
        return
    
    def reverse(self):
        if self.head is None:
            print("List is empty")
        
        curr = self.head
        prev = None
        nnext = None
        
        while curr is not None:
            nnext = curr.next
            curr.next = prev
            prev = curr
            curr = nnext
        
        self.head = prev
        print("List is reversed")
        return
    
    def delete_at_start(self):
        print("deleteing at the start of the list")
        if self.head is None:
            print("Nothing to delete")
        
        curr = self.head
        self.head = curr.next
        return
    
    def delete_at_end(self):
        print("deleting at the end of the list")
        if self.head is None:
            print("Nothing to delete")
        
        curr = self.head
        prev = None
        while curr.next is not None:
            prev = curr
            curr = curr.next
        prev.next = None
        return
    
    def count_list(self):
        print("Counting the list")
        if self.head is None:
            print("List is empty")
            
        curr = self.head
        cnt = 0
        while curr is not None:
            cnt += 1
            curr = curr.next
        print(cnt)
        return cnt
    
    def insert_at_specific(self,data,pos):
        print("Inserting data at position -" + str(pos))
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        cnt=self.count_list()
        if pos > cnt:
            print("provide a valid position")
            return

        if pos == 1:
            new_node.next = self.head
            self.head = new_node
            return
        curr = self.head
        prev = None
        c = 0
        while curr is not None:
            c += 1
            if c == pos:
                new_node.next = curr
                curr = new_node
                prev.next = curr
            else:
                prev = curr
                curr = curr.next
        return        
    
llist = LinkedList()
llist.insert_at_start(20)
llist.insert_at_start(4)
llist.insert_at_end(15)
llist.insert_at_end(85)
llist.insert_at_end(50)
llist.traverselist()

llist.reverse()
llist.traverselist()
llist.count_list()
llist.insert_at_specific(12,3)
llist.traverselist()