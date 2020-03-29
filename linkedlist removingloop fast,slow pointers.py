#node class
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
#linkedlist class
class LinkedList:
    def __init__(self):
        self.head=None
    #function to create newnode and inserting it into linkedlist
    def insert(self,newdata):
        newnode=Node(newdata)
        if self.head is None:
            self.head=newnode
            return
        lastnode=self.head
        while(lastnode.next):
            lastnode=lastnode.next
        lastnode.next=newnode
    #printing linkedlist elements
    def printllist(self):
        currentnode=self.head
        if currentnode is None:
            print("linkedlist is empty")
        while(currentnode):
            print(currentnode.data)
            currentnode=currentnode.next
    #function for detecting loop
    def detect_loop(self):
        slow=fast=self.head
        while (slow and fast and fast.next):
            slow=slow.next
            fast=fast.next.next
            if(slow==fast):
                print("loop is present")
                self.removeloop(slow)
                return
        print("loop is not present")
        return
    #function for removing loop in linkedlist
    def removeloop(self,refnode):
        pointer1=self.head
        while(True):
            pointer2=refnode
            while(pointer2.next is not pointer1 and pointer2.next is not refnode):
                pointer2=pointer2.next
            if pointer2.next is pointer1:
                break
            pointer1=pointer1.next
        pointer2.next=None

if __name__=="__main__":
    llist=LinkedList()
    for i in range(1,7):
        llist.insert(i)
    #creatingloop in linkedlist
    llist.head.next.next.next.next.next.next=llist.head
    llist.detect_loop()
    llist.printllist()

    
            
        