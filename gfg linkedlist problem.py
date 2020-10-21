#problemlink:https://practice.geeksforgeeks.org/problems/linked-list-length-even-or-odd/0/?category[]=Linked%20List&difficulty[]=-1&page=1&query=category[]Linked%20Listdifficulty[]-1page1
def isLengthEvenOrOdd(head):
    # Code here
    currentnode=head
    count=1
    while(currentnode.next!=None):
        currentnode=currentnode.next
        count+=1
    if count%2==0:
        return True
    else:
        return False