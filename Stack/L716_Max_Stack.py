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
