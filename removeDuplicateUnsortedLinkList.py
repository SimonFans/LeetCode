class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkList:
    def __init__(self):
        self.head=None
    def push(self,newdata):
        new_node=Node(newdata)
        new_node.next=self.head
        self.head=new_node

    def removeDuplicated(self):
        if self.head is None:
            return self.head
        curr=self.head
        while curr:
            inner=curr
            while inner.next:
                if inner.next.data==curr.data:
                    inner.next=inner.next.next
                else:
                    inner=inner.next
            curr=curr.next
        return self.head


    def printList(self):
        temp=self.head
        while temp:
            print(temp.data)
            temp=temp.next

test=LinkList()
test.push(4)
test.push(2)
test.push(2)
test.push(1)
print(test.printList())

test.removeDuplicated()
print(test.printList())


