class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class sll:
    def __init__(self):
        self.head=None

#Node Insertion at beggining 

    def insert_begining(self,data):
        nb=Node(data)
        nb.next=self.head
        self.head=nb

#Insertion at end

    def insert_end(self,data):
        ne=Node(data)
        tmp=self.head
        while tmp.next:
            tmp=tmp.next
        tmp.next=ne

#insertion at particular position

    def insert_pos(self,data,pos):
        np=Node(data)
        tmp=self.head
        for i in range(pos-1):
            tmp=tmp.next
        np.data=data
        np.next=tmp.next
        tmp.next=np
        
#Displaying Nodes

    def display(self):
        tmp=self.head
        if tmp is None:
            print("Linked list is empty")
        while tmp:
            print(tmp.data,"--->",end="")
            tmp=tmp.next

l=sll()
n1=Node(10)
l.head=n1
n2=Node(20)
n1.next=n2
n3=Node(30)
n2.next=n3
l.insert_begining(5)
l.insert_end(40)
pos=int(input("Enter position :"))
l.insert_pos(35,pos)
l.display()
