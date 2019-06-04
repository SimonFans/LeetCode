This problem was asked by Amazon.

Given a linked list, remove all consecutive nodes that sum to zero. Print out the remaining nodes.

For example, suppose you are given the input 3 -> 4 -> -7 -> 5 -> -6 -> 6. In this case, you should first remove 3 -> 4 -> -7, then -6 -> 6, leaving only 5.

# X -> 3 -> 4 -> -7 -> 5 -> -6 -> 6

class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
        
class solution:
    def remove_sum_zero(self,head):
        dummy=Node(0)
        dummy.next=head
        cur=head
        res=dummy
        while cur:
            temp_sum=cur.val
            temp=cur.next
            while temp:
                temp_sum+=temp.val
                if temp_sum==0:
                    cur=temp
                    dummy.next=temp.next
                    dummy=temp.next
                    temp_sum=0
                    break
                temp=temp.next
            cur=cur.next
            
        while res.next:
            print(res.next.val)
            res=res.next

                           
node1=Node(3)
node2=Node(4)
node3=Node(-7)
node4=Node(5)
node5=Node(-6)
node6=Node(6)

node1.next=node2
node2.next=node3
node3.next=node4
node4.next=node5
node5.next=node6

head=node1
print(solution().remove_sum_zero(head))
