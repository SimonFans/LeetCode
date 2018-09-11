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

    def delete(self,target):
        temp=self.head
        if temp is None:
            return
        if temp is not None:
            if temp.data==target:
                self.head=temp.next
                temp=None
                return
        while(temp is not None):
            if temp.data == target:
                break
            prev=temp
            temp=temp.next
        prev.next=temp.next
        temp=None

    def printList(self):
        temp=self.head
        while temp:
            print(temp.data)
            temp=temp.next

test=LinkList()
test.push(4)
test.push(3)
test.push(2)
test.push(1)
print(test.printList())
test.delete(2)
print(test.printList())


