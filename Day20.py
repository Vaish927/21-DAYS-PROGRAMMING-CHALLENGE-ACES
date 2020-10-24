def delat(self,position):
        currentnode=self.head
        currentpos=0
        while(True):
            if(currentpos==position):
                previousnode=currentnode.next
                currentnode.next=None
                break
            previousnode=currentnode
            currentnode=currentnode.next
            currentpos+=1