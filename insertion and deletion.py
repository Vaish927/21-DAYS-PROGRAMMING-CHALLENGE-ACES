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


    def insertat(self,newnode,position):
        if position == 0:
            self.insertashead(newnode)
            return 
        currentnode=self.head
        #previousnode=self.head
        currentpos=0
        while True:
            if(currentpos==position):
                previousnode.next=newnode
                newnode.next=currentnode
                break
            previousnode=currentnode
            currentnode=currentnode.next
            currentpos+=1


    def insertashead(self,newnode):
        tempnode=self.head
        self.head=newnode
        self.head.next=tempnode
        del tempnode
    def delend(self):
        lastnode=self.head
        while(lastnode.next is not None):
            previousnode=lastnode
            lastnode=lastnode.next
        previousnode.next=None