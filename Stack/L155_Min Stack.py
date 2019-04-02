Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
Example:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.

# Method 1:

class MinStack:

    def __init__(self):
        self.stack1=[]
        self.stack2=[]
    
    def push(self, x):
        self.stack1.append(x)
        if len(self.stack2)==0 or x<=self.stack2[-1]:
            self.stack2.append(x)
        
    # @return nothing
    def pop(self):
        top=self.stack1[-1]
        self.stack1.pop()
        if top==self.stack2[-1]:
            self.stack2.pop()

    # @return an integer
    def top(self):
        return self.stack1[-1]        

    # @return an integer
    def getMin(self):
        return self.stack2[-1]



# Method 2:
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack=[]
        

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> None:
         del self.stack[-1]        
            
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return min(self.stack)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

