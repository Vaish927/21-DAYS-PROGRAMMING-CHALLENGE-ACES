class Node :
    def __init__(self,name):
        self.name=name
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
    def insert(self,newnode):
        if self.head is None:
            self.head=newnode
        else:
            lastnode=self.head
            while(True):
                if lastnode.next is None:
                    break
                lastnode=lastnode.next
            lastnode.next=newnode
    def printlist(self):
        if self.head.next is None:
                print("List is empty")
                return
        currentNode=self.head
        while True:
            if currentNode is None:
                break
            print(currentNode.name)
            currentNode=currentNode.next
        print("Finished")

            

        
a=Node("Monday")
b=linkedlist()
b.insert(a)
c=Node("Tuesday")
b.insert(c)
d=Node("Wednesday")
b.insert(d)
b.printlist()

