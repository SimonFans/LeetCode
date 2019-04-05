Design a max stack that supports push, pop, top, peekMax and popMax.

 

push(x) -- Push element x onto stack.
pop() -- Remove the element on top of the stack and return it.
top() -- Get the element on the top.
peekMax() -- Retrieve the maximum element in the stack.
popMax() -- Retrieve the maximum element in the stack, and remove it. If you find more than one maximum elements, 
only remove the top-most one.
 

Example 1:

MaxStack stack = new MaxStack();
stack.push(5); 
stack.push(1);
stack.push(5);
stack.top(); -> 5
stack.popMax(); -> 5
stack.top(); -> 1
stack.peekMax(); -> 5
stack.pop(); -> 1
stack.top(); -> 5
 

Note:

-1e7 <= x <= 1e7
Number of operations won't exceed 10000.
The last four operations won't be called when stack is empty.


class MaxStack(object):  
   def __init__(self):  
     """  
     initialize your data structure here.  
     """  
     self.l = []  
     self.maxL = []  

   def push(self, x):
     """  
     :type x: int  
     :rtype: void  
     """  
     self.l.append(x)  
     if not self.maxL:  
       self.maxL.append(x)  
     else:  
       self.maxL.append( max(x, self.maxL[-1]) )  
     return  

   def pop(self):
     """  
     :rtype: int  
     """  
     v = self.l.pop()  
     self.maxL.pop()  
     return v  

   def top(self):
     """  
     :rtype: int  
     """  
     return self.l[-1]  

   def peekMax(self):
     """  
     :rtype: int  
     """  
     return self.maxL[-1]  

   def popMax(self):
     """  
     :rtype: int  
     """  
     maxValue = self.maxL[-1]  
     poppedValues = []  
     v = self.pop()  
     while v != maxValue:  
       poppedValues.append(v)  
       v = self.pop()  
     for v in poppedValues[::-1]:  
       self.push(v)  
     return maxValue


stack=MaxStack()
stack.push(5)
stack.push(1)
stack.push(5)
print(stack.top())
stack.popMax()
stack.top()
stack.peekMax()
stack.pop()
stack.top()
