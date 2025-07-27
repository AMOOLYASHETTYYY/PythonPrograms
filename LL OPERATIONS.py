
class node:
    def __init__(self,data):
        self.next=None
        self.data=data
class LinkedList:
    def __init__(self):
        self.head=None
    def add_data(self,data):
        newnode=node(data)
        if self.head is None:
            self.head=newnode
        else:
            temp=self.head
            while(temp.next!=None):
                temp=temp.next
            temp.next=newnode
    def display(self):
        temp=self.head
        while(temp):
            print(temp.data,end="->")
            temp=temp.next
    def delete(self,a):
        if self.head==None:
            print("no node to be deleted")
            return
        if a==1:
            temp=self.head
            self.head=temp.next
        else:
            prev=None
            cur=self.head
            for i in range(1,a):
                prev=cur
                cur=cur.next
                if cur==None:
                    print("element doesnt exist ")
                    return
            prev.next=cur.next

l=LinkedList()
l.add_data(20)
l.add_data(28)
l.add_data(30)
l.add_data(40)
l.delete(2)
l.display()
