Design a max stack that supports push, pop, top, peekMax and popMax.

---
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
     self.stack1 = []
     self.stack2 = []

   def push(self, x):
     """
     :type x: int
     :rtype: void
     """
     self.stack1.append(x)
     if len(self.stack2)==0 or x>=self.stack2[-1]:
         self.stack2.append(x)
     return

   def pop(self):
     """
     :rtype: int
     """
     top = self.stack1[-1]
     self.stack1.pop()
     if top == self.stack2[-1]:
         self.stack2.pop()
     return top

   def top(self):
     """
     :rtype: int
     """
     return self.stack1[-1]

   def peekMax(self):
     """
     :rtype: int
     """
     return self.stack2[-1]

   def popMax(self):
     """
     :rtype: int
     """
     maxValue = self.stack2[-1]
     poppedValues = []
     v = self.stack1.pop()
     while v != maxValue:
       poppedValues.append(v)
       v = self.stack1.pop()
     for v in poppedValues[::-1]:
       self.stack1.push(v)
     return maxValue


stack=MaxStack()
print(stack.push(5))
print(stack.push(1))
print(stack.push(5))
print(stack.top())
print(stack.popMax())
print(stack.top())
print(stack.peekMax())
print(stack.pop())
print(stack.top())
